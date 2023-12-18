from tkinter import TRUE
import requests
import xml.etree.ElementTree as ET


url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

options = {
    "Content-Type": "text/xml; charset=utf-8",
}
iterator="y"
while iterator=="y":
    countryname=input("Введите название страны: ")
    SOAPEnvelope = f"""
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryISOCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryName>{countryname}</sCountryName>
        </CountryISOCode>

      </soap:Body>
    </soap:Envelope>
    """

    response= requests.post(url, data = SOAPEnvelope, headers = options)

    root = ET.fromstring(response.text)
    
    for child in root.iter("{http://www.oorsprong.org/websamples.countryinfo}CountryISOCodeResult"):
        isocode = child.text

    print("Код ISO страны: ",isocode)

    characteristics=["CapitalCity","CountryIntPhoneCode","CountryCurrency"]
    data=[]

    for char in characteristics:
        SOAPEnvelope = f"""
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <{char} xmlns="http://www.oorsprong.org/websamples.countryinfo">
              <sCountryISOCode>{isocode}</sCountryISOCode>
            </{char}>
      </soap:Body>
    </soap:Envelope>
    """
        response2= requests.post(url, data = SOAPEnvelope, headers = options)
        root = ET.fromstring(response2.text)
        
        text="{http://www.oorsprong.org/websamples.countryinfo}"+f"{char}Result"
        if char==characteristics[-1]:

            text="{http://www.oorsprong.org/websamples.countryinfo}sName"
        for child in root.iter(text):
            ct=str(child.text)
            data.append(ct)

    print("Столица: "+data[0]+"\n"+"Телефонный код страны: "+data[1]+"\n"+"Валюта: "+data[2])

    iterator=input("Продолжить работу?: ")
