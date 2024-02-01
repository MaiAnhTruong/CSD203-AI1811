from Car import *
from Node import *
from BSTree import MyQueue
class Q2_3:
    flag = True
    def check(self, x):
        return x<7
    deleteNode =None
    count =0
    def breadth_first2(self,tree):
        if tree.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(tree.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if (p.left!=None and p.right!=None and self.check(p.data.Price) and self.flag ):
                # self.flag = False
                self.deleteNode =p
                self.count +=1
                if self.count ==1:
                    self.flag = False
                    break;
            # self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        # print("")        
    #end def
    def deleteByCopyingLeft(self, p):
        if  p==None or p.left ==None : 
            return
        if p.left.right==None:
            p.data = p.left.data
            p.left = p.left.left  
            return
        cur = p.left.right
        father =p.left
        while cur.right:  
            father = cur
            cur = cur.right  
        p.data = cur.data
        father.right = cur.left 
    def f3(self,tree):
        self.breadth_first2(tree)  
        self.deleteByCopyingLeft(self.deleteNode)  