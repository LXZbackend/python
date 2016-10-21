# coding=utf-8
def bubbleSort(list):
    for num in range(len(list) - 1, 0, -1):  # 外层循环需要循环 列表长度的-1次，
        for i in range(num):  # 注意这里面循环只要到最后num 在下面的判断中 因为是
            # 上一个和下个匹配    当你到达前一个的时候其实 就可以对比到最后一个了。但那是选择排序不一样 所以得 加1
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

    print list


if __name__ == '__main__':
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(myList)
