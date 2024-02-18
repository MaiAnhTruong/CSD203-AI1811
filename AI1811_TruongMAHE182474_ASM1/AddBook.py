def add_book(library):
    bid = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    node = Node(bid, title, author)
    library.add_node(node)
    print(f"Book {title} added successfully.")
    