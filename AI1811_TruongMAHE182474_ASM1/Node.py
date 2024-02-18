class Node:
    def __init__(self, bid, title, author, status=None, borrower=None):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status if status is not None else "available"
        self.borrower = borrower
        self.next = None