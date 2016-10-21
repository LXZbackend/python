#coding=utf-8
#生成器  以及yield的使用

# 这是自己模拟 xrange(num) 这个会生

def myxrange(num):
	i = 0
	while i<num:
		resut = yield i
		print resut
		if resut =="hello":
			print('world')

		else:
			print("resut is null ")
		i+=1



if __name__ == '__main__':
	my = myxrange(5)
	my.next()



# def gen():
# 	for x in xrange(4):
# 		temp = yield x


# 		if temp =="hello":
# 			print"world"
# 		else:
# 			print "temp is  null"