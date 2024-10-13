 
from flask import Flask, request
from suds.client import Client

app = Flask(__name__)


WSDL = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = Client(WSDL)

@app.route('/soap', methods=['POST'])
def soap_service():
   

    soap_request = request.data
    print("Gelen SOAP İsteği:")
    print(soap_request)

 
    response = client.service.Add(5, 10)  # 5 + 10 işlemi

    print("Gönderilen SOAP Yaniti:")
    print(response)

    # SOAP cevabını döndür
    return f"Sonuç: {response}", 200

if __name__ == "__main__":
    app.run(debug=True)
