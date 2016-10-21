#coding=utf-8
from time import ctime, sleep
# 写一个装饰器，能记录被装饰函数的访问时间和调用者。（调用者模拟传入,记录文件自己创建，追加操作）

# 首先编写一个装饰器  他的功能就是显示 他被谁调用
def use_time_fun(func):

	def wrappedfunc():
		# 声明两个变量用于存储存储被调用的函数名字和时间
		
		user = func.__name__
		time = ctime()
		print("%s called at %s"%(user,time))
		write_file(user,time)
		return func()

	return wrappedfunc








def write_file(user,time):
	f = open("./log.txt",'a')

	write_info = "function:"+user +"在"+time+"访问"+"\n"
	f.write(write_info)

	f.close()

# #decorator2.py
# from time import ctime, sleep

# def timefun(func):
#     def wrappedfunc(a, b):
#         print("%s called at %s"%(func.__name__, ctime()))
#         print(a, b)
#         return func(a, b)
#     return wrappedfunc

@use_time_fun
def foo():
    print("foo函数来过。。。。。。。")



@use_time_fun
def person():
	print ("person 函数表示我也来过。。。。。")





if __name__ == '__main__':
	foo()
	person()