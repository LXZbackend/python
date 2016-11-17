#coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
from tornado.options import define,options
from tornado.web import url,RequestHandler
import torndb
import os

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		stu  = {
		"name":"zhangsan",
		"age":24,
		"gender":1,
		}
		# 序列化
		stu_json = json.dumps(stu)
		self.set_header("Content_Type","application/json;charset=utf-8")
		self.write(stu_json)

		self.send_error(404,err_content='lixainzhu',err_title='haha')

		# self.set_status(444,'lixianzhu error')
		# self.write(stu)
class InsertHandler(tornado.web.RequestHandler):

	def post(self):
		name = self.get_argument('name')
		passwd = self.get_argument('passwd')
		mobile = self.get_argument('moblie')
		sql = "insert into it_user_info(ui_name,ui_passwd,ui_mobile) value(%(name)s,%(passwd)s,%(mobile)s)"
		user_id = self.application.db.execute(sql,name=name,passwd=passwd,mobile=mobile)
		
		







class Application(tornado.web.Application):
    def __ini__(self,*args,**kwargs):
        super(Application,self).init(*args,**kwargs)
        self.db = torndb.Connection(
        host = '127.0.0.1',
        database = 'itcast',
        user = 'root',
        password = 'mysql'

        )



if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    settings = dic(
    static_path = os.path.join(current_path,'static'),
    template_path = os.path.join(current_path,'template'),
    )



	app =Application([
	url(r'/',IndexHandler,name='myobject')],**settings)

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)


	tornado.ioloop.IOLoop.current().start()
