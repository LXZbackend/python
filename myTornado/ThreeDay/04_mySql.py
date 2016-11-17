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
		ret = self.application.db.get("select ui_name from it_user_info where ui_user_id=1")
		print ret
		self.write(ret['ui_name'])





	def post(self):
		print '00000000000'
		name = self.get_argument('name')
		passwd = self.get_argument("passwd")
		mobile = self.get_argument('moblie')
		area = self.get_argument('area')
		print '1111111111111111111111'
		print name,passwd,mobile,area
		# 注这里里面要用

		# sql = "inset into it_user_info(ui_name,ui_passwd,ui_moblie) values(%(name)s, %(passwd)s, %(mobile)s)"
		sql = "insert into it_user_info(ui_name, ui_passwd, ui_mobile,ui_area_id) values(%(name)s, %(passwd)s, %(mobile)s,%(area)s)"
		try:
			print"xiammmmmmm"
			user_id = self.application.db.execute(sql, name=name, passwd=passwd, mobile=mobile,area=area)
			print 'id',user_id
		except Exception as e:
			print e
		
		self.write('111')


class InserHandler(BaseHandler):

	def get(self):
		print '1111111111111111111111'
		# ret = self.application.db.get("select ui_name from it_user_info where ui_user_id=1")
		# print ret
		self.write('11111111')




	def post(self):
		print '00000000000'
		name = self.get_argument('name')
		passwd = self.get_argument("passwd")
		mobile = self.get_argument('moblie')
		area = self.get_argument('area')
		print '1111111111111111111111'
		print name,passwd,mobile
		# 注这里里面要用

		sql = "inset into it_user_info(ui_name,ui_passwd,ui_moblie,ui_area_id) values(%(name)s,%(passwd)s,%(mobile)s,%(area)s)"
		try:
			user_id = self.application.db.execute(sql,name=name,passwd=passwd,mobile=mobile,area=area)
		except Exception as e:
			print '22222222222222222'
			print"进去了"
		self.write(str(user_id))





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
		(r"/insert",InserHandler),
		(r'/house',HouseHandler),

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
