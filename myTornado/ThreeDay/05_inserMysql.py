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
        # print"这里执行了prepare"
        # 这里有一个问题 你怎么那么笨呢?GET如果没有的话,你得给一默认值啊,不然找不到,肯定没有startwith方法啊  
        if self.request.headers.get("Content-Type",'').startswith("application/json"):
          self.json_dict = json.loads(self.request.body)
        else:
          self.json_dict = None
# 
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
        #这是查询数据库中的多个值 返回的是一个列表
        ret = self.application.db.query("select ui_name,ui_mobile from it_user_info where ui_age between 10 and 20;")
        # print ret 
        print type(ret)
        for temp in ret:
            self.write(temp['ui_name'])
            self.write(temp['ui_mobile'])
            self.write('\n')
        # self.write(ret)


    def post(self):
        '''
            插入数据,


        '''
        name = self.get_argument('name')
        passwd = self.get_argument("passwd")
        moblie = self.get_argument('moblie')
        area = self.get_argument('area')

        # 编写sql 插入语句
        sql = "insert into it_user_info(ui_name,ui_passwd,ui_mobile,ui_area_id) value(%(name)s,%(passwd)s,%(moblie)s,%(area)s)"

        try:
            user_id = self.application.db.execute(sql,name=name,passwd=passwd,moblie=moblie,area=area)
            # print user_id
        except Exception as e:
            print e
        # self.write(user_id)

class HouseHandler(BaseHandler):
    def get(self):
        user_id = self.get_argument('user')
        print "这是传进来的用户id",user_id
        sql = "select ui_name,ui_mobile,hi_address,hi_price,hi_name from it_user_info  left  join it_house_info  on ui_user_id=hi_user_id where ui_user_id=%s"

      
        try:
           ret =self.application.db.query(sql,user_id)
        except Exception as e:
            print e
            self.write({"error":1,"errmse":"sql error","data":[]})

        houses = []
        print ret
        print type(ret)
        '''
        查询的是一个列表类型,里面存的的是类字典类型
        这时候查询出来的就已经是一个列表了,列表中哦个每一个元素都是一个字典,但是字典的键是数据库中的字段,不能这样就这样返回
        这里不能直接将数据返回给前端,不然,就让前端知道数据库字段了.所以我们需要自己封装一个
        名字
        '''

        # for info in ret:
        #     house={
        #         'uname':info['ui_name'],
        #         'tel':info['ui_mobile'],
        #         'hname':info['hi_name'],
        #         'haddr':info['hi_address'],
        #         'hpirc':info['hi_price']

        #     }
        #     houses.append(house)
        self.write({'error':0,"errmsg":'OK',"data":ret})
        # self.write({"errno":0, "errmsg":"OK", "data":houses})





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
        (r'/house',HouseHandler),



    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
