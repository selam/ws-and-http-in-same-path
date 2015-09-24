#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import web
from tornado import websocket
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop 

class HttpHandler(web.RequestHandler):

     def get(self):
        if self.request.headers.get("Sec-Websocket-Version", None) != None:
           self.set_header("X-Accel-Redirect", "/ws") 
           self.finish()
           return
	self.render("index.html")


class WebSocketHandler(websocket.WebSocketHandler):


    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"



if __name__ == "__main__":
   application = web.Application(handlers=[(r"/", HttpHandler), (r"/ws", WebSocketHandler)])
   server = HTTPServer(application)
   server.listen(2222)
   IOLoop.instance().start()




