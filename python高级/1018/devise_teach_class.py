#coding=utf-8
'''
	设计讲师和学生类，讲师有上课，备课等方法，
	学生有听课，做练习等方法，均有姓名、性别、年龄等基本属性

'''


class Person(object):
	def __init__(self,name,sex,age):
		self._name = name
		self._sex = sex
		self._age = age

	@property
	def name(self):
		return self._name


	@name.setter
	def name(self,name):
		self._name =name

	@property
	def age(self):
		return self._age


	@age.setter
	def age(self,age):
		self._age =age





class Student(Person):

	def listenClass(self):
		print("%s我在听课。。。"%self._name)



	
	
class Teacher(Person):

	def in_class(self):
		print ("%s老师正在上课"%self._name)


	def plan_class(self):
		print ("%s老师正在备课"%self._name)
			





if __name__ == '__main__':
	Myste = Student("lisi","man",21)
	Myste.listenClass()
	print Myste.name
	print Myste.age
	


	Mytea = Teacher("dongge",'sex',22)
	Mytea.in_class()

	print Mytea.name
	Mytea.age = 32
	print Mytea.age 
	







