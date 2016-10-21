#coding=utf-8
import random
import re
# 数7游戏，把一个随机100个数里面，含7和7的倍数的值提取出来。（提示:filter）

# 首先生成一百个随机数
def producting_random_num(len):
	#先用一个列表存储生成的数字
	list_num = []

	i = 0
	# 通过传入的值 确认生成的个数
	while i<len:
		num = random.randint(1,1000)
		# num = str(num)
		list_num.append(num)
		i+=1

	return list_num


# 编写处理函数
def judeg_exist_num(num):
	# 对传入的数据进行处理 首先是除以7 如果得出0 那么就是 ，如果不是 对每一位进行除以10 看是否为7  如果是则存起来 如果不是 进行下一个
	flag = False
	# 该函数主要功能是判断是否能被7整除

	if(num%7==0):
		flag = True
	# 如果不满足 就判断每一位是否含有7
	else:
		num = str(num)
		for i in num:
			# print i
			if(i == "7"):
				flag = True
	return flag




	'''
		第二中方法
		# 编写一个正则 用于匹配字符串是否存在7
		 r=re.match(".+?(\d+-\d+-\d+-\d+)",s)

		 r = re.match("")
	'''



if __name__ == '__main__':
	# 调用函数生成指定的长度的随机数
	random_list= producting_random_num(100)

	print "这是生成的随机数列表",random_list
	#filter 这个内建函数中第一个传的是一个函数 如果返回true  就把后面列表中 存起来 用一个列表中 
	result_num = filter(judeg_exist_num,random_list )
	print "这是处理后的列表",result_num


	

		

