# coding: utf-8
import web
import json
import datetime
from datetime import *

from main import collection
from bson.objectid import ObjectId
from main import render

class CJsonEncoder(json.JSONEncoder):
    '''
    针对date datetime 序列化处理
    '''
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def formatField(data):
    '''
    格式化字段
    :param data:
    :return:
    '''
    data['_id'] = str(data['_id'])
    data['post_date'] = eval(json.dumps(data['post_date'], cls=CJsonEncoder))
    return data

class TD(object): #针对待办事件列表 处理类

    def POST(self):
        '''
        新建待办事件
        :return:
        '''
        i = web.input()
        print i
        title = i.get('title', None)
        if not title:
            return json.dumps({'error':'标题让你吃了吗？'})

        post_data={
            'title':title,
            'post_date':datetime.now()
        }
        collection.insert_one(post_data)
        format_data = formatField(post_data)
        web.header('Content-Type', 'application/json')
        return json.dumps(format_data)

    def GET(self):
        '''
        查看待办事件
        :return:
        '''
        i = web.input()
        print i
        page = int(i.get('page', 1))
        limit = int(i.get('limit', 10))
        skip_num = (page-1)*10
        results = []
        for post_data in collection.find().skip(skip_num).limit(limit):
            format_data = formatField(post_data)
            results.append(format_data)
        #web.header('Content-Type', 'application/json')
        #return json.dumps(results)
        return render.index(results)

def get_by_id(id):
    '''
    按ID查询数据库
    :param id:
    :return:
    '''
    s = collection.find_one({'_id':ObjectId(id)})
    if not s:
        return False
    return s

class TD_Simple: #针对单个待办事件处理类

    def GET(self, id):
        '''
        按ID查询返回结果
        :param id:
        :return:
        '''
        #web.header('Content-Type', 'application/json')
        todo = get_by_id(id)
        if not todo:
            return json.dumps({'error':'没找到这条记录'})
        format_data = formatField(todo)
        #return json.dumps(format_data)
        return render.edit(todo)


    def PATCH(self, id):
        '''
        按ID查询修改结果
        :param id:
        :return:
        '''
        todo = get_by_id(id)
        web.header('Content-Type', 'application/json')
        if not todo:
            return json.dumps({'error':'没找到这条记录'})
        i = web.input()
        print i

        title = i.get('title', None)
        status = i.get('finished', None)

        if title :
            collection.update({'_id': ObjectId(id)}, {"$set": {'title': title}})
        if status:
            if status.lower() == 'yes':
                finished = True
            elif status.lower() == 'no':
                finished = False
            collection.update({'_id': ObjectId(id)}, {"$set": {'finished': finished}})
        if not title and not status:
            return json.dumps({'error':'您发起了一个不允许的请求'})

        #修改成功
        todo = get_by_id(id)
        format_data = formatField(todo)
        return json.dumps(format_data)


    def DELETE(self, id):
        '''
        按ID删除结果
        :param id:
        :return:
        '''
        web.header('Content-Type', 'application/json')
        todo = get_by_id(id)
        if not todo:
            return json.dumps({'error':'没找到这条记录'})
        collection.remove({'_id':ObjectId(id)})
        return json.dumps({})

