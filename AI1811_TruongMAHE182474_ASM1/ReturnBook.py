def return_book(library):
    bid = input("Enter book id to return: ")
    if library.return_book(bid):
        print("Book returned successfully.")
    else:
        print("Book not found or not borrowed.")