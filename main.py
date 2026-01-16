from book import Book
from member import Member

books = []
members = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    books.append(Book(book_id, title, author))
    print("Book added successfully")

def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    members.append(Member(member_id, name))
    print("Member registered successfully")

def borrow_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book.book_id == book_id and not book.is_borrowed:
            book.is_borrowed = True
            print("Book borrowed successfully")
            return
    print("Book not available")

def display_records():
    print("\nBooks:")
    for book in books:
        status = "Borrowed" if book.is_borrowed else "Available"
        print(book.book_id, book.title, status)

    print("\nMembers:")
    for member in members:
        print(member.member_id, member.name)

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Display Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        add_member()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        display_records()
    elif choice == "5":
        break
    else:
        print("Invalid choice")