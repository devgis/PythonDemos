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

asmxurl="http://192.168.5.222:8001/HFSWS.asmx"
methodName="HisTransData" 
#values = {'xml':str}  
#params = urllib.urlencode(values)
#param="xml="+str
#str=str.replace('&','&amp;')
#str=str.replace('<','&lt')
#str=str.replace('>','&gt;')

param ="<?xml version=\"1.0\" encoding=\"utf-8\"?>"
param+="<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">"
param+="  <soap:Body>"
param+="    <HisTransData xmlns=\"http://tempuri.org/\">"
param+="      <xml>"+str+"</xml>"
param+="    </HisTransData>"
param+="  </soap:Body>"
param+="</soap:Envelope>"

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
webservice = httplib.HTTP("192.168.5.222","8001",30)
#连接到服务器后的第一个调用。它发送由request字符串到到服务器
webservice.putrequest("POST", "HFSWS.asmx") #HTTP/1.1
webservice.putheader("Host", "localhost")
#webservice.putheader("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)")
webservice.putheader("Content-type", "text/xml; charset=utf-8")
webservice.putheader("Content-length", "%d" % len(SoapMessage))
webservice.putheader("SOAPAction", "\"http://tempuri.org/HisTransData\"")

#发送空行到服务器，指示header的结束
webservice.endheaders()
#发送报文数据到服务器
webservice.send(SoapMessage)
#获取返回HTTP 响应信息
statuscode, statusmessage, header = webservice.getreply()

print "Response: ", statuscode, statusmessage
print "headers: ", header
res = webservice.getfile().read()
print res

#SoapMessage=SoapMessage %(sn,pwd,mobile,context)
   #使用的WebService地址为sdk.entinfo.cn:8061/webservice.asmx，
#   webservice = httplib.HTTP("sdk.entinfo.cn:8061")
   #连接到服务器后的第一个调用。它发送由request字符串到到服务器
#   webservice.putrequest("POST", "/webservice.asmx")
#   webservice.putheader("Host", "sdk.entinfo.cn:8061")
#   webservice.putheader("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)")
#   webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
#   webservice.putheader("Content-length", "%d" % len(SoapMessage))
#   webservice.putheader("SOAPAction", "\"http://entinfo.cn/mdsmssend\"")
   #发送空行到服务器，指示header的结束
#   webservice.endheaders()
   #发送报文数据到服务器
#   webservice.send(SoapMessage)
   #获取返回HTTP 响应信息
#   statuscode, statusmessage, header = webservice.getreply()
#   return statuscode


#url = "http://192.168.5.222:8001/HFSWS.asmx/HisTransData"
#values = {'xml':str}  
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
#headers = { 'User-Agent' : user_agent,"Content-type": "application/x-www-form-urlencoded" }   
#data = urllib.urlencode(values)   
#req = urllib2.Request(url,data, headers)   
#response = urllib2.urlopen(req)   
#the_page = response.read()   
