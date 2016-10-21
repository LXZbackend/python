#coding=utf-8
def quickSort(alist,first,last):
	if first<last:
		splitpoint  = findpos(alist,first,last)

		quickSort(alist,first,splitpoint-1)
		quickSort(alist, splitpoint+1, last)


def findpos(lists,low,high):
	key = lists[low]
	while low<high:
		while low<high and lists[high]>key:

			high -= 1

		lists[low] = lists[high]

		while  low<high and lists[low]<key:
			low += 1
		lists[high] = lists[low]

	lists[low] = key

	return low


if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	quickSort(alist,0,8)#这得手打传入 第一和最后一位。
	print(alist)