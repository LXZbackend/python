class SingleNode:
	def _init_(self,item):
		self._item = item
		self._next = None
	# 创建一个方法 用于获取节点的内容
	def getItem(self):
		return self._item

	# 获取下个节点的地址 用指针
	def getNext(self):

		return self._next
	#设置 下一个节点的指向
	def setNext(self,newNext):

		self._next = newNext
	




class SingleLinkList:
	# 定义一个指向单向链表的头指针
	def _init_(self):
		self._head = None;

	#创建一个获取列表长度的方法 通过判断节点是否为空 
	def size(self):
		current = self._head
		count = 0
		# 这里面可能有个疑惑  为啥不是判断当前节点下一个是否空的
		# 而判断当前节点是否上是空的。我是这么理解的。因为你从头节点开始。你只能获取第一个节点 
		# 这时候你直接获取下一个节点  万一没有下一个节点呢？你这时候长度初始化为0 难道你返回0？
		# 加入这时候只有一个节点时就会报错。所以 直接判断当前节点/
		while current !=None:
			count+=1
			current=current.getNext()
		return count

# 定义一个函数 用于判断链表是否为空  
# 这时候只需要判断头节点指向是否是空的就行
	def isEmpty(self):
		return self._head ==None

	# 遍历链表  就是打印出每个节点的值

	def travel(self):
		current = self._head
		while current!=None:
			print current.getItem()
			current = current.getNext()


# 链表头部添加节点
	def add(self,item):
		# 首先添加的话 你得创建一个节点
		temp = SingleNode(item)
		# 设置这个节点的下一个指向，指向头节点指向的那个元素
		temp.setNext(self._head)
		# 让头节点指向该节点
		self._head = temp

# 链表的尾部添加节点
	def append(self,item):
		# 首先还是创建节点
		temp = SingleNode(item)
		# 判断节点是否是空的 如果是否的这时候就头节点指向该节点
		if self.isEmpty():
			self._head = temp

		#如果不是的话还是不停的遍历 
		else:
			current = self._head
			# 找到当前节点的下一个节点是否为空
			# 不为空  继续向下移动
			while current.getNext()!=None:
				current = current.getNext()

			# 当找到下一个节点为空的时候  循环会终止，这时候current就是最后一个节点 只需要让他指向当前节点就行/
			current.setNext(temp)


	# 查找链表中某个值是否存在 返回ture  false
	# 遍历呗  挨个对比
	def search(self,item):
		current = self._head
		# 设置一个标志位
		founditem = False
		while current!=None and not founditem:
			if current.getItem()==item:

				founditem = True

			else:
				current = current.getNext()
		return founditem



	# 删除链表中的节点
	def remove(self,item):
		current = self._head

		pre = None
		# 循环遍历这个链表 找到对应的值
		while current!=None:
			if current.getItem()==tiem:
				# 如果是第一个节点
				if not pre:
					 #将头指针指向头节点的后一个节点
				self._head = current.getNext()
				else:
					# 将要删除节点的第一个节点的指针指向改节点之后的一个节点
					pre.setNext(current.getNext())
				break

			else:
				# 就继续按链表后移动节点
				pre = current
				current = current.getNext()

	def insert(self,pos,item):
		if pos<=1:
			self.add(item)
		elif pos>self.size():
			self.append(item)
		else:
			temp = SingleNode(item)
			count = 1

			#pre用于记录要插入pos位置之前的一个节点
			pre = None
			# 从头指针指向的节点开始
			current = self._head
			# 当前位置小于要插入的位置
			while count<pos:
				count+=1
				pre=current
				current = current.getNext()
		  #设置第pos-1个位置的下一个节点为temp
            pre.setNext(temp)
            #设置temp的下一个节点为pos+1个节点
            temp.setNext(current)



'''
	对最后的count <pos 进行总结分析 因为你是从count=1开始的 所以循环的时候进去后加加1 
	这时候哪两个指针就已经移动了 
	当 count=1 时current指向第一个位置 pre 指向它之前那个元素
	同理 等count =2 时 再进去循环 这时候位置 current 指向2 

	假如插入的位置是3  这时候count =3哪两个指针一个指向 3  一个指向之前的

	这时候就不能再往后面到移动 也就是条件不能再满足了 也就是不能有等号
	如果有等号 他就还会往后面移动 这时候指向的位置就不对了







'''