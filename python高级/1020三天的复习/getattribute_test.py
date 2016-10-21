#coding=utf-8
class Itcast(object):
    name = 'lixianzhu'
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器，打log
    def __getattribute__(self,obj):
        if obj == 'name':
            print"name"
            print('log self.subject1')
            return 'redirect python'
        else:   #测试时注释掉这2行，将找不到subject2
            print object.__getattribute__(self,obj)
            return object.__getattribute__(self,obj)

    def show(self):
        print 'this is Itcast'

s = Itcast('python')
# print s.name
print Itcast.name
print s.subject2