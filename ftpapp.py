## -*- coding:utf-8 -*-  
__author__='xinlan'
from tornado import web,ioloop,httpserver
#application = web.Application
#application=web.Application([])
class MainPageHandler(web.RequestHandler):
  def get(self,*args, **kwargs):
      self.write('欢迎到达海龙的公司')
application=web.Application([
             (r"/index1",MainPageHandler),
])
if __name__== '__main__':
   http_server=httpserver.HTTPServer(application)
   http_server.listen(6969)
   ioloop.IOLoop.current().start()
