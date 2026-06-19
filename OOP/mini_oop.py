class Book():
    def __init__(self, title, author, isbn, is_borrowed = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        
class Members():
    def __init__(self, name, member_id, borrowed_books:list):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        
    def borrowed_book(self, book):
        book.is_borrowed = True
        self.borrowed_books.append(book)
        return book

    
    def return_book(self, book):
        if book.is_borrowed:
            book.is_borrowered = False
            self.borrowered_books.pop(book)
        else:
            return False
        
class Library():
    def __init__(self, book = [], members = []):
        self.books = book
        self.members = members 
        
    def add_book(self, book): 
        self.books.append(book)
        print(f'Successfully added {book.title}')
        
    def register_member(self, member):
        self.members.append(member)
        print(f'Successfully added {member.name}')
        
    def show_available_book(self):
        return self.books
        
        

book1 =  Book("HIM", "Eric", "478928456")
book2 =  Book("Which Way", "Eric", "238472648")
book3 =  Book("The Way", "Eric", "758493028")

member1 = Members("Mr Obi", "LIB_231", [])
member2 = Members("Mrs Chioma", "LIB_592", [])
member3 = Members("Mr oke", "LIB_683", [])

library1 = Library()

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

print("\nAvailable books")
for book in library1.show_available_book():
    print(book.title)

print("\nNew members")
library1.register_member(member1)
library1.register_member(member2)
library1.register_member(member3)


# print()

        