import os
import httplib
import json
import urllib

baiduapi="192.168.5.222:8001"
src="/HFSWS.asmx/HisTransData"
 
def load2(xml):
    try:
        params = urllib.urlencode({
            'xml': xml
        })
        headers = {
            "POST":"/HFSWS.asmx HTTP/1.1",
            "Host":"192.168.5.222",
            "Content-type":"application/soap+xml; charset=utf-8",
            "Content-length": "%d" % len(xml),
            #"SOAPAction":"http://tempuri.org/HisTransData",
            "Accept": "text/plain"
        }
        conn = httplib.HTTPConnection(baiduapi)
        conn.request("POST", src, params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        return data
        conn.close()
    except Exception ,e:
        print e
        return ""

SM_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <HisTransData xmlns="http://tempuri.org/">
      <xml>%s</xml>
    </HisTransData>
  </soap:Body>
</soap:Envelope>
"""

SM_TEMPLATE2="""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <HisTransData xmlns="http://tempuri.org/">
      <xml>%s</xml>
    </HisTransData>
  </soap12:Body>
</soap12:Envelope>
"""

# 打开一个文件
fo = open("E:\\Work\\WSES\\HFSWS\\HFSWS.Test\\bin\\Debug\\xmls\\prescription.xml", "r+")
str = fo.read()
str=str.replace(" ","")
str=str.replace("\n", "")
str=str.replace('&','&amp;')
str=str.replace('<','&lt')
str=str.replace('>','&gt;')
SoapMessage = SM_TEMPLATE2%(str)
print SoapMessage
print load2(SoapMessage)