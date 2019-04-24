#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 

import os
import base64
import urllib
import urllib2
import httplib

# 打开一个文件
fo = open("E:\\Work\\WSES\\HFSWS\\HFSWS.Test\\bin\\Debug\\xmls\\prescription.xml", "r+")
str = fo.read()
str=str.replace(" ","")
str=str.replace("\n", "")


SM_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <HisTransData xmlns="http://tempuri.org/">
      <xml>%s</xml>
    </HisTransData>
  </soap:Body>
</soap:Envelope>
"""

SoapMessage = SM_TEMPLATE%(str)

#print SoapMessage
asmxurl="http://192.168.5.222:8001/HFSWS.asmx"
methodName="HisTransData" 

#test_data = {'xml':str}
#test_data_urlencode = urllib.urlencode(test_data)
headerdata = {"POST":"/HFSWS.asmx HTTP/1.1","Host":"192.168.5.222","Content-type":"text/xml; charset=utf-8","Content-length": "%d" % len(SoapMessage),"SOAPAction":"http://tempuri.org/HisTransData"}
conn = httplib.HTTPConnection("192.168.5.222",8001,10)
conn.request(method="POST",url="/HFSWS.asmx",body=SoapMessage,headers = headerdata) 
response = conn.getresponse()
res= response.read()
print res