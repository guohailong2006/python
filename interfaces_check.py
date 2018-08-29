#coding:utf-8
import requests,re,sys,os

def get_url():
  import re
  url='http://www.quanmin.tv/x/app/tabs?cid=6&client=2&type=2'
  get=requests.get(url)
  content=get.content
  re=re.compile(r'{"code":0,"message":"","data":(.*)')
  find=re.findall(content)
  kongzhi='[]'
  #global right_num,error_num,a
  #right_num=1
  #error_num=0
  if find != kongzhi:
      return 1
  else:
      return 0

def get_name():
    global name
    name = os.path.basename(__file__)
def shuchu():
    get_name()
    number=get_url()
    rename='/root/monitor/'+name+'.yml'

    with open(rename,'w') as f:
        f.write(name+'  '+str(number))
        f.close()
shuchu()
