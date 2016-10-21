class Person(object):
	def __init__(self,name,age,taste):
		self.name = name
		self._age = age
		self.__taste = taste



	def showPerson(self):
		print(self.name)
		print (self._age)
		print(self.__taste)


	def _work(self):
		print ("in——work")

	def __awag(self):
		print("in__awag")




def student(Person):


	def showtu(self):
		print(self.name)
		print(self._age)
		print(self.__taste)

	def showstudent(self):
		print("*"*10)
		super(student,self).showPerson()
		print("*"*10)

	def testParent(self):
		self.showPerson()
		self._work()
		self.__awag()