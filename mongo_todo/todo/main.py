# coding: utf-8
import web

urls = (
    '/renderTest', 'Test',
    '/', 'index',
    '/TodoLists', 'todo.TD',
    '/TodoLists/(\w+)', 'todo.TD_Simple',
   
)
render = web.template.render('templates')

class Test(object):
    def GET(self):
        return render.showRender('hello world')

class index(object):
    def GET(self):
        return "Hello, world!"

    def POST(self):
        i = web.input()
        print i

    def PUT(self):
        i = web.input()
        print i

from pymongo import MongoClient

# Making a Connection with MongoClient
client = MongoClient('localhost', 27017)
# Getting a Database
db = client['todo-db']
# Getting a Collection
collection = db['TodoLists']

config = web.storage(
    email='piaosanlang@gmail.com',
    site_name = '任务跟踪',
    site_desc = '',
    static = '/static',
)
web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()