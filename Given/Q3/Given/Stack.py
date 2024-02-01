class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def top(self):
        return self.head.data
    def push(self,data):
        n = Node(data)
        if self.isEmpty():
            self.head = n
        else:
            n.next = self.head
            self.head = n
    def pop(self):
        if self.isEmpty():
            return None
        value = self.head.data
        self.head = self.head.next
        return value                        