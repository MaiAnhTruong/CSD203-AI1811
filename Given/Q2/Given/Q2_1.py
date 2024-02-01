from Car import *
from Node import *

class Q2_1:
    def f1(self,tree,name, price=-1):
        if name[0] =="B" or price >100: return
        node = Node(Car(name,price)) 
        if tree.isEmpty():
            tree.root = node
            return
        cur = tree.root
        father = None
        while cur:
            if cur.data.Price ==price:
                # print(f"key {data} is exist ");
                return
            else:
                father = cur
                if cur.data.Price <price:
                    cur = cur.right
                else:
                    cur = cur.left
        if father.data.Price<price:
            father.right = node    
        else:
            father.left =  node