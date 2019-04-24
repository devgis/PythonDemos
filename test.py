#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 

import os
# 打开一个文件
fo = open("text.txt", "wb")
fo.write( "liyafei!\n")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
fo = open("text.txt", "r+")
str = fo.read(10)
#os.mkdir("E:\\newdir2")

os.chdir("E:\\temp")
print os.listdir("E:\\temp")
print "读取的字符串是 : ", str