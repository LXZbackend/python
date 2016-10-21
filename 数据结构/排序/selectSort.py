# coding=utf-8as
def selectSort(list):
    # 注意这里为啥要长度-1 因为最后一次其实已经排好了  这时候你再执行其实就没啥用了  还有为啥要
    # 从大到小的减少，其实还是为了方便内层的循环执行的次数  因为内层循环测试每次减1
    for index in range(len(list) - 1, 0, -1):
        position = 0
        # 这里是从列表中第二个开始的 因为以及标记每次第一个是最大的  所以从第二个开始，这里index+1 是为了能操作到最后一个
        for i in range(1, index + 1):
            if list[position] < list[i]:
                position = i

        temp = list[position]
        list[position] = list[index]
        list[index] = temp

    print list
    # return list

if __name__ == '__main__':

    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    selectSort(myList)
