from Car import *
from Node import *
class Q1_2:
    def f2(self, linkList, name="", price=-1):
        node = Node(Car(name,price))
        if linkList ==None:
            linkList.head = linkList.tail = node
        else:
            node.next = linkList.head
            linkList.head = node
                
