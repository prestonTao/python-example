# -*- coding:utf-8 -*-

'''
Created on 2015年6月15日

@author: Administrator
'''
import os

from tornado import ioloop
import tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index")

url_patterns = [(r'/', MainHandler),
]


#路径获取
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

#tonado基本配置
settings = {
#     'debug': options.debug,
#     'static_path': location("./status"),
#     'media_path':location("./media"),
#     'cookie_secret': "vZS/c+BKTASaEjrBJ51uMMX+AwCyp0bcmXHOlX0jd0s=",#base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
#     'cookie_expires': 1,  # cookie will be valid for this amount of days
#     'xsrf_cookies': True,
    'login_url': '/user/login/',
}

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(
            url_patterns, *args,  **dict(settings.settings, **kwargs))

app = Application(url_patterns)
app.listen(8888, "127.0.0.1")
ioloop.IOLoop.instance().start()


