#coding=utf-8
# 这个文件的作用是 探究 类的私有属性 以及个各下划线 
class Person(object):
	def __init__(self,name,age,taste):
		self.name = name
		self._age = age
		self.__taste = taste

	def showperson(self):
		print(self.name)
		print(self._age)
		print(self.__taste)


	def _work(self):
		print("in_work")

	def __awag(self):
		print("in __awag")


class Student(Person):
	def construction(self,name,age,taste):

		self.name = name
		self._age = age
		self.__taste = taste

	def testparent(self):
		self.showperson()
		self._work()
		self.__awag()


	def showtu(self):
		print(self.name)
		print(self._age)
		print(self.__taste)

	def showstudent(self):
		print("*"*10)
		super(Student,self).showperson()
		Person.__awag(self)
		# super(Student,self).__awag()
		print("*"*10)



	@staticmethod
	def debug(self):
		_Debug.showbug()





class _Debug(object):

	@staticmethod
	def showbug():
		print('in showbug')
















