class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete_node(self, bid):
        if self.head is None:
            return
        if self.head.bid == bid:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.bid == bid:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(f"{current.bid} | {current.title} | {current.author} | {current.status}")
            current = current.next

    def borrow_book(self, bid):
        current = self.head
        while current:
            if current.bid == bid and current.status == "available":
                current.status = "issued"
                return True
            current = current.next
        return False

    def return_book(self, bid):
        current = self.head
        while current:
            if current.bid == bid and current.status == "issued":
                current.status = "available"
                return True
            current = current.next
        return False