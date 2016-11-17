# coding=utf-8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import os
import json
import torndb
from tornado.web import RequestHandler, url, StaticFileHandler
from tornado.options import options, define


class BaseHandler(RequestHandler):

	def prepare(self):
		pass
		# 这里有一个问题 
		# if self.request.headers.get("Content-Type").startswith("application/json"):
		# 	self.json_dict = json.loads(self.request.body)
		# else:
		# 	self.json_dict = None

	def set_default_headers(self):
			 # 设置get与post方式的默认响应体格式为json
		self.set_header("Content-Type", "application/json; charset=UTF-8")
		# 设置一个名为itcast、值为python的header
		self.set_header("itcast", "python")

	def write_error(self, status_code, **kwargs):
		pass

	def initialize(self):
		pass

	def on_finish(self):
		pass


class IndexHandler(BaseHandler):

	def get(self):
		self.write('lixianzh')


class Application(tornado.web.Application):
	'''
			自己重写Application 在这里设置数据库的参数
	'''

	def __init__(self, *args, **kwargs):
		super(Application, self).__init__(*args, **kwargs)

		# 设置数据库的基本信息
		# 增加db这个对象
		self.db = torndb.Connection(
			host="127.0.0.1",
			database='itcast',
			user='root',
			password='mysql'
		)


if __name__ == '__main__':
	current_path = os.path.dirname(__file__)
	settings = dict(
		static_path=os.path.join(current_path, 'static'),
		template_path=os.path.join(current_path, 'templates'),
		debug=True
	)

	app = Application([

		(r'/', IndexHandler),



	], **settings)

	'''
	这里要注意理解   有两种启动方式,app.listen() 和下面
	http_server = tornado.httpserver.HTTPServer(app) 这两个方式

	app.listen(8000) 这一句话其实包含两句话,其实就是
	 http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8000)
	这时候加入你要开启多个服务,
	等于又把http_server.listen(8000)  这句话拆成两句话
	http_server.bind(8000)
	http_server.start(0)

	所以两种方式都是可以将实例app 传到 RequestHandler 这里面
	self.application.db.

	'''

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8000)
	tornado.ioloop.IOLoop.current().start()
