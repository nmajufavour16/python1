import random

class Book:
    def __init__(self, title, author, ISBN, is_borrowed=False):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_borrowed = is_borrowed
    
    def available_books(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nISBN: {self.ISBN} \nIs borrowed: {self.is_borrowed}"

class Member:
    def __init__(self, name, member_id, borrowed_books:list):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books


class Library:
    def __init__(self, books, members, register_member, show_available_books):
        self.books = books
        self.members = members
        self.register_member = register_member
        self.show_available_books = show_available_books
        
    def show_available_books(self, book):
        for book in self.books:
            print(book.available_books())  
        return f"Books: {self.books} \nMembers: {self.members} \nRegister member: {self.register_member} \nShow available books: {self.show_available_books}"
    
    def register_member(self, name, member_id):
        self.name = input("Enter your name: ")
        self.member_id = random.int(100000000, 999999999)
        [] = input("Would you like to borrow a book? (Y/N): ")
        if [] == "Y":
            print(self.show_available_books("Pick a book: "))
            book = input("Enter the book's ISBN: ")
            self.books.append(book)

    
book1 = Book("Python101", "Mr.John", "123456789", True)
book2 = Book("Python for Beginners", "Mr. Uche", "234567891", False)
book3 = Book("Python: Introduction to OOP", "Miss. Promise", "345678912", False)

member1 = Member("Phayvo", "987654321", [book2, book3])
member2 = Member("Laufey", "876543219", [book1, book2])
member3 = Member("Eze", "765432198", [book1, book2, book3])

library1 = Library()

library1.register_member(member1)
library1.register_member(member2)
library1.register_member(member3)

# print("Welcome to Mai Lyebrary")
# print("What would you like to do today?")
# print("1. Register as a member \n2. Show available books \n3. Borrow a book \n4. Return a book")
# option = input("Enter your option: ")
# if option == "1":
#     print(Library.register_member())
# elif option == "2":
#     print(Library.show_available_books())