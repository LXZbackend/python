# coding: utf-8
from pymongo import MongoClient

# Making a Connection with MongoClient
client = MongoClient('localhost', 27017)
# Getting a Database
db = client['todo-db']
# Getting a Collection
collection = db['TodoLists']

import datetime

collection.remove({})
collection.insert_one({
            'title':'增加摘要功能，除标题外还可以写描述',
            'post_date':datetime.datetime.strptime('2011-06-03 06:08:10','%Y-%m-%d %H:%M:%S')
        })
collection.insert_one({
            'title':'增加分类，不同的事项划分到不同的分类中去',
            'post_date':datetime.datetime.strptime('2011-06-03 06:08:37','%Y-%m-%d %H:%M:%S')
        })
collection.insert_one({
            'title':'不直接删除，改为完成，标示为该条事项已完成显示在最下方',
            'post_date':datetime.datetime.strptime('2011-06-03 06:09:18','%Y-%m-%d %H:%M:%S')
        })
collection.insert_one({
            'title':'这是一条测试',
            'post_date':datetime.datetime.strptime('2011-06-04 23:00:47','%Y-%m-%d %H:%M:%S')
        })
collection.insert_one({
            'title':'这是一条测试2',
            'post_date':datetime.datetime.strptime('2011-06-04 23:01:31','%Y-%m-%d %H:%M:%S')
        })



