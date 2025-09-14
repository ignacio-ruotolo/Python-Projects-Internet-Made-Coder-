# Create a library system using classes that allows you to track books and users.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print("The book has been checked out.")

    def return_book(self):
        self.is_checked_out = False
        print("The book has now been returned.")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # list of Book objects

    def borrow_book(self, book):
        if not book.is_checked_out:
            self.borrowed_books.append(book)
        else:

    def return_book(self, book):
        if book.is_checked_out:
            self.borrowed_books.append(book)
        else:
