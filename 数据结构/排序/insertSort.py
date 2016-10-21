#coding= utf-8
# 插入排序
def insertSort(list):
	'''
		这里面又不减1了 为啥因为冒泡和选择都是把最大的往后面插入，经过他们的比较 最后一个其实已经是排序好的 这时候其实还比不比较无所谓了，但是插入排序，他前几次的交换 都不涉及到后面的数值，所以他需要比较到最后面一个，跟前面的挨个比较。

	'''
	for index in range(1,len(list)):
		tempvalue = list[index]

		position = index

		while position>0 and tempvalue<list[position-1]:
			list[position] = list[position-1]
			position -=1



		list[position] = tempvalue

if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	insertSort(alist)
	print(alist)