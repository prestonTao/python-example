# -*- coding: utf-8 -*-
'''
Created on 2015年6月5日

@author: Administrator
'''
import os

import tornado
from tornado.options import options


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index")

url_patterns = [
    (r"/", MainHandler),
]

#路径获取
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

#tonado基本配置
settings = {
    'debug': options.debug,
    'static_path': location("./status"),
    'media_path':location("./media"),
    'cookie_secret': "vZS/c+BKTASaEjrBJ51uMMX+AwCyp0bcmXHOlX0jd0s=",#base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    'cookie_expires': 1,  # cookie will be valid for this amount of days
    'xsrf_cookies': True,
    'login_url': '/user/login/',
}


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(
            url_patterns, *args, **dict(settings.settings, **kwargs))


if __name__ == "__main__":
        app=Application()
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port,options.address)
        print 'start service '+options.address+":"+str(options.port)
        tornado.ioloop.IOLoop.instance().start()
