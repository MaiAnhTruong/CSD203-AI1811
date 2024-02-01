from Car import *
from Node import *
class Q1_1:
    
    def f1(self, linklist, name="", price=-1):
        if name.startswith("B") or price >100:
            return
        n = Node(Car(name,price))
        if (linklist.isEmpty()):
            linklist.head = linklist.tail = n
        else:
            linklist.tail.next = n
            linklist.tail = n    