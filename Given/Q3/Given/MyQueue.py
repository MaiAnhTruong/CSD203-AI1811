class NodeQ:
    def __init__(a,data):
        a.data = data
        a.next = None
class MyQueue:
    def __init__(a):
        a.head = None
        a.tail = None
    def isEmpty(a):
        return a.head ==None
    def EnQueue(a, data):
        node = NodeQ(data)
        if a.isEmpty():
            a.head = node
            a.tail = node
        else:
            a.tail.next = node
            a.tail = node
    #end def
    def DeQueue(a):
        if a.isEmpty():
            return None
        data = a.head.data
        a.head = a.head.next
        return data
#end class    
