from flask import Flask, request
from flask_restx import Api, Resource
from suds.client import Client

app = Flask(__name__)
api = Api(app, version='1.0', title='SOAP Service API',
          description='SOAP Service API')



WSDL = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = Client(WSDL)

@api.route('/soap')
class SoapService(Resource):
    @api.doc(description='SOAP servisi için bir istek')
    def post(self):
        

        soap_request = request.data
        print("Gelen SOAP İsteği:")
        print(soap_request)


        response = client.service.Add(5, 10)  # 5 + 10 işlemi

        print("Gönderilen SOAP Yaniti:")
        print(response)

        # SOAP cevabını döndür
        return {"result": response}, 200

if __name__ == "__main__":
    app.run(debug=True)
