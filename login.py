#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__='hailong'
wechat='735973239'
def write():
  list=[]
  f=open('login.txt','a')
  #加入\n的写法这样可以让
  f.write('\n'+login)
  f.close() 
  return;
def init():
  ##理解global的使用规范，我们认为在任何变量如果不是局部，我们就应该早早定义成global变量
###或许我们后续会调用这个变量
  global login,fr
  login=raw_input('please input your login_name')
  fp=open('login.txt','r')
  fr=fp.read()
  #global login
  fp.close()
for i in range(3):
    init()
    if login in fr:
        print "login success and your name is ",login
        break
    else:
        write()
        print "your login is not ok,try again，u has tried ",i
