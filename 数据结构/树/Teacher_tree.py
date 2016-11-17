class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem == -1:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            # 对已有的节点进行层次遍历
            while myQueue:
                # 弹出队列的第一个元素
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
	            else:
	                #如果左右子树都不为空，加入队列继续判断
	                myQueue.append(treeNode.lchild)
	                myQueue.append(treeNode.rchild)
    def front(self, root):
      """递归实现先序遍历"""
      if root == None:
          return
      print root.elem
      self.front(root.lchild)
      self.front(root.rchild)

    def middle(self, root):
      """递归实现中序遍历"""
      if root == None:
          return
      self.middle(root.lchild)
      print root.elem
      self.middle(root.rchild)

    def later(self, root):
      """递归实现后续遍历"""
      if root == None:
          return
      self.later(root.lchild)
      self.later(root.rchild)
      print root.elem


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)