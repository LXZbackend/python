# coding=utf-8
# 冒泡排序


def bobbleSort(list):
    # 首先设置外层循环
    # 逐渐递减 最后也循环长度减1次 但是为内存循环提供了方便
    for i in range(len(list) - 1, 0, -1):
    # 注意这里面循环只要到最后num 在下面的判断中 因为是上一个和下个匹配 当你到达前一个的时候其实 就可以对比到最后一个了。但那是选择排序不一样 所以得 加1
        for j in range(i):
            if list[j + 1] < list[j]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp

    print "这是冒泡排序", list


def selectSort(list):
    # 选择排序是对冒泡排序的更行  他不需要每次都换值 大大减小了 交换的开支，只执行一次交换
    for i in range(len(list) - 1, 0, -1):
        maxindex = 0
         # 这里是从列表中第二个开始的 因为以及标记每次第一个是最大的  所以从第二个开始，这里index+1 是为了能操作到最后一个 
        for j in range(1, i + 1):
            if list[maxindex] < list[j]:
                maxindex = j

        temp = list[i]
        list[i] = list[maxindex]
        list[maxindex] = temp

    print "这是选择排序", list


def insertSort(list):
    # 插入排序就是 把第一个当做有序序列 从第二

if __name__ == '__main__':
    testlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bobbleSort(testlist)
    selectSort(testlist)
