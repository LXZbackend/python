# coding=utf-8
class Node(object):
    '''
       create node class
    '''

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    '''

                    Tree class
                    思路：思路：有点像上次的链表，创建单个节点，个链表类，把单个链表添加到链表类中。
                    当你初始化一Tree对象时，会创建一个新的根节点，用上面的创建的节点对象创建

                    然后你在主函数，循环的添加，add()  当你第一个数进来时，这时候根节点是-1的，所以让传进来的第一个数当做
                    根节点，然后第二个数进来，这时候有一个队列用来存储，叶子节点，就是当左右孩子都有的时候，然后就把他的孩子添加到这个队列中
                    下次再进来就会弹出他的孩子节点，为他孩子节点添加左右孩子

                    第一次第一次没想明白的地方：为啥每次都要把根节点放在哪个队列中？？？？这时候要注意每次进来之后都是把列表清空，
                    他每次插入都是从新走一遍，就是说从上到下的判断一次，看有没有空的，如果没有就把他孩子再添加到队列中，知道找空的，
                    插入，下次进来的时候 上次插入的节点已经被弹出去了，这时候列表也已经重置为空，就从根节点，一点点往下看看，
                    拿着根看左右节点是否有值，如果有就把自己的左右孩子添加到队列。where继续循环 弹出下一个，拿着去看左右，。。。。一直这样。
                    一直找到左右有一个孩子没有的。结束循环，从新执行add 方法


    '''

    def __init__(self):
        self.root = Node()

    def add(self, elem):
        '''
                        add node for tree
        '''
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem == -1:
            self.root = node

        else:
            myQueue = []
            treeNode = self.root
            # print"rootNode",treeNode
            # print type(treeNode.elem)
            # print dir(treeNode.elem)
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


  	


if __name__ == '__main__':

    tree = Tree()
    for i in range(10):
        node = Node(i)
        print node.elem
        tree.add(node)
