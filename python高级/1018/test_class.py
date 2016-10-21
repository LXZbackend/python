#coding=utf-8
# 该代码主要是看类属性和实例属性
_ssss = "123"
class person(object):
	__name = "lixianzhu"


	def __init__(self,age):
		self._age = age

class Teach(person):

	def printName(self):
		print(self.__name)



if __name__ == '__main__':
	per = Teach(16)
	# per.printName()
	print per._age
	# print per.age
	# print dir(per)


	# print(per.name)
	# person.name = "taoyuling"
	# print person.name
	# per.name = "yuxiaoshuang"
	# print "实例",per.name
	# print "类",person.name 