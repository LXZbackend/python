class SingleNode():
    def __init__(self,item):
        self._item=item
        self._next=None
    #获取节点的值
    def getItem(self):
        return self._item
    #获取下一个指针
    def getNext(self):
        return self._next
    #设置下一个节点
    def setNext(self,newnext):
        self._next=newnext

class SingleLinkedList():  
    #定义一个头单向链表的头指针
    def __init__(self):
        self._head=None
    #判断链表是否为空
    def isEmpty(self):
        return self._head==None

    #链表的长度
    def size(self):
        current=self._head
        count=0
        #当链表不为空
        while current!=None:
            count+=1
            #将current后移一个节点
            current=current.getNext()
        return count

    #遍历链表
    def travel(self):
        #将头节点赋给current
        current=self._head
        while current!=None:
            #打印当前节点的值
            print current.getItem()
            current=current.getNext()

    #链表头部添加节点
    def add(self,item):
        #新建一个节点
        temp=SingleNode(item)
        #新节点的下一个节点为头指针指向的值
        temp.setNext(self._head)
        #将新节点设置为头指针指向的节点
        self._head=temp

    #链表尾部添加节点
    def append(self,item):
        temp=SingleNode(item)
        if self.isEmpty():
            self._head=temp
        else:
            current=self._head
            #当前节点的下一个节点不为空
            while current.getNext()!=None:
                current=current.getNext()
            #最后一个节点的下一个节点为要添加的节点
            current.setNext(temp)

    #链表查找节点是否存在，并返回True或者False
    def search(self,item):
        current=self._head
        founditem=False
        while current!=None and not founditem:
            if current.getItem()==item:
                founditem=True
            else:
                current=current.getNext()
        return founditem           

    #删除链表中的节点
    def remove(self,item):
        current=self._head
        pre=None
        while current!=None:
            if current.getItem()==item:
                #如果第一个就是删除的节点
                if not pre:
                    #将头指针指向头节点的后一个节点
                    self._head=current.getNext()
                else:
                    #将要删除节点的前一个节点的指针指向该节点之后的一个节点
                    pre.setNext(current.getNext())
                break
            else:
                #就继续按链表后移节点
                pre=current
                current=current.getNext()     

    #在指定位置插入节点
    def insert(self,pos,item):
        if pos<=1:
            self.add(item)
        elif pos>self.size():
            self.append(item)
        else:
            temp=SingleNode(item)
            count=1
            #pre用于记录要插入pos位置之前的一个节点
            pre=None
            #从头指针指向的节点开始
            current=self._head
            #当前位置小于要插入的位置
            while count<pos:
                count+=1
                pre=current
                current=current.getNext()
            #设置第pos-1个位置的下一个节点为temp
            pre.setNext(temp)
            #设置temp的下一个节点为pos+1个节点
            temp.setNext(current)