def borrow_book(library):
    bid = input("Enter book id to borrow: ")
    if library.borrow_book(bid):
        print("Book borrowed successfully.")
    else:
        print("Book not available for borrowing.")