#!/usr/bin/python
# -*- coding: UTF-8 -*-
fn=r'../1.txt'
fp=open(fn,'rw')
#cont=fp.read()
#print fp.read()
for i in fp.readline():
  print i
print "你好"
