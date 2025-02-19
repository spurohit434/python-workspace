from utils import database

User_Menu =  """
- 'a' to add books
- 'l' to list books
- 'r' to remove books
- 'q' to quit
Enter your choice: 
"""

def menu():
    choice = input(User_Menu)
    while choice!= 'q':
        if choice == 'a':
            add_book()
        elif choice == 'l':
            list_book()
        elif choice == 'q':
            pass
        else:
            print("Invalid choice enter valid choice")
        choice = input(User_Menu)




def add_book():
    name = input("enter the name of the book")
    author = input("enter the author of the book")
    database.add_book(name, author)

def list_book():
    books = database.read_book()
    print(books)

menu()