from Car import *
from Node import *
from BSTree import MyQueue
class Q2_4:
    flag = True
    def check(self, x):
        return x<7
    RotateNode =None
    count=0
    def f4(self, tree):
        self.breadth_first3(tree)
        if self.RotateNode ==None:
            return
        self.rightRotation(tree, self.RotateNode.data)
    #end def    
    def breadth_first3(self,tree):
        if tree.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(tree.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if (p.left!=None and self.check(p.data.Price) and self.flag ):
                # self.flag = False
                self.RotateNode =p
                self.count +=1
                if self.count ==1:
                    self.flag = False
                    break;
            # self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
    #end def  
    def findFather(self,tree, data):
        if tree.root.data.Price == data:
            return None  
        fa = None  
        cur = tree.root
        while cur:            
            if cur.data.Price == data:
                return fa
            fa = cur    
            if cur.data.Price<data:
                cur = cur.right
            else:
                cur = cur.left
        return None  
    #end def
    def rightRotate(self,p):        
        if not p or not p.left:
            return
        c = p.left
        p.left = c.right
        c.right = p
        return c 
    def rightRotation(self, tree, data):
        f = self.findFather(tree,data.Price)        
        p = None
        if f == None:
            if (tree.root.data !=data):
                return
            else:
                p = tree.root
        else:
            if (f.data.Price>data.Price):
                p = f.left
            else:
                p = f.right  
        newNode = self.rightRotate(p) 
        if f ==None:
            self.root = newNode
        else:
            if (f.data.Price<data.Price):
                f.right = newNode
            else:
                f.left = newNode             