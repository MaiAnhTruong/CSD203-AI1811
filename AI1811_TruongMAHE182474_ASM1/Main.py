from Node import Node
from LinkedList import LinkedList
from AddBook import add_book
from ViewBooks import view_books
from DeleteBook import delete_book
from BorrowedBook import borrow_book
from ReturnBook import return_book

def main():
    library = LinkedList()
    while True:
        print("1. Add book")
        print("2. View books")
        print("3. Delete book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            delete_book(library)
        elif choice == '4':
            borrow_book(library)
        elif choice == '5':
            return_book(library)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()