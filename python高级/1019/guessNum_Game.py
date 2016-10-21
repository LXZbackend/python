#coding=utf-8
import random

class GuessNum(object):
	'''
		这个类是是一个猜数的类 
		思路：
			猜的数是随机产生的，并且可以设置猜的次数，如果没传参数 就默认猜15
			随机数要求：首先数是四位数 四位数 数字不能重复，
			用户输入的方法：首先对首先对用户输入的 进行判断，长度 或者是否都是数字 或者够不够四位 
			匹配函数规则：如果每对应上一个数字和位置 就在输出的字符串上添加一个A ,如果只是
			含有这个数字  则返回一个B 其他的数字什么都不返回
			另为：如果用户输入exit 就代表放弃  这时候就需要推出循环 把正确的值告诉他

	'''


	def __init__(self,num=15):
		'''
			构造方法
		'''
		self._num = num
		self._randomNum = self.Creat_random()
	

	def Creat_random(self):
		'''
			要求：生成的四位数不能重复  方法 用一个random.choice 从序列中获取一个随机数
			再把每次选中的随机数从列表中删除

		'''
		numList = range(0,10)
		# 创建一个循环变量 用于控制生成的位数
		i = 0
		randomNum = ''
		while i<4:
			# 通过方法在 一个序列中随机选取一个数字
			num = random.choice(numList)
			numList.remove(num)
			randomNum +=str(num)
			# print randomNum
			i+=1
		# print "ss",randomNum
		return randomNum


	def judge_input(self,userinput):
		'''
			这时候传入的合法的数字，对他进行判断

		'''
		# 定义一个下标变量，用来同时控制两个字符串相对应的字符是否相等
		# 测试代码
		# self._randomNum ='1234'


		userinput = str(userinput)
		if userinput ==self._randomNum:
			print"恭喜你猜对了！"
			return 'AAAA'
		else:
			index = 0
			print_info = ''
			while index<4:
				# print 	self._randomNum[index],userinput[index]
				if 	self._randomNum[index] == userinput[index]:
					print_info +='A'
				elif userinput[index] in self._randomNum:
					print_info +='B'
				
				index+=1
			# 这时候输出的字符串 AB 顺序没有调整，可以通过输出看出端倪。这样不行

			# 这时候对字符串转换成列表 再用列表的sort排序 然后在转换成字符串输出
			templist = []
			for  i in print_info:
				templist.append(i)

			# 对输入的进行排序
			templist.sort()
			# 再转换成字符串输出


			outStr = ''.join(templist)
			print outStr’

			return outStr




			# print print_info



	def user_input(self):
		'''
			这个方法主要数对用户输入的 进行判断，首先判断是否是退出的命令 如果不是在判断是
			长度数否够4位，在判断否是数字 
		'''
		# 提示信息
		print "如果放弃，请输入exit"
		user_input = raw_input("请输入你猜得的数字：")
		# print ()
		len_input = len(user_input)

		if len_input!=4:
			print "您输入的有误，请重新输入"
			

		elif user_input == "exit":
			return "exit"
		elif user_input.isdigit() and self.judge_repeat(user_input):
			return user_input
		else:
			print  "您输入数字有重复，请重新输入！！！"


	def judge_repeat(self,str):
		mystr = ''
		for i in str:
			if i not in mystr:
				mystr+=i
		if len(mystr)==4:
			return True
		else:
			return False


	def start(self):
		'''
			这是游戏的开始入口函数

		'''
		# 调用函数 
		self.Creat_random()
		while 1:
			user_num = self.user_input()
			# print"您输入的是",mynum
			if user_num=="exit":
				print "生成的随机数为：",self._randomNum
				break
			flag = self.judge_input(user_num)
			if flag =="AAAA":
				break
		



			
if __name__ == '__main__':
	g = GuessNum()

	print g._randomNum
	# g.judge_input("8712")
	g.start()