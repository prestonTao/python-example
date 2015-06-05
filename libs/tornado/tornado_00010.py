# -*- coding:utf-8 -*-
'''
Created on 2015年6月4日

@author: Administrator
'''
import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


class Excn(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(403)

class Params(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name",None)
        self.write(name)

class Redirect(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/", permanent=True)


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),   # url正则匹配
    (r"/exception", Excn),                # 返回403错误
    (r"/params", Params),                 # 获取参数
    (r"/redirect", Redirect),             # 重定向
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
