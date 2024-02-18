def delete_book(library):
    bid = input("Enter book id to delete: ")
    library.delete_node(bid)
    print(f"Book with id {bid} has been deleted.")