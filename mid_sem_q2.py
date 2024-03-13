class Book:
    def __init__(self, title, author, publication_year, availability=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = availability

class Library:
    def __init__(self):
        self.inventory = []

    def add(self, book_name, author, publication_year):
        new_book = Book(book_name, author, publication_year)
        self.inventory.append(new_book)
        print(f"{new_book.title} added to the library inventory.")

    def available_books(self):
        print("\nAvailable Books:")
        for book in self.inventory:
            if book.availability:
                print(f"{book.title} by {book.author} ({book.publication_year})")

    def remove(self, book_name):
        for book in self.inventory:
            if book.title == book_name:
                self.inventory.remove(book)
                print(f"{book.title} removed from the library inventory.")
                return
        print(f"Book not found: {book_name}")

    def search(self, book_name):
        print(f"\nSearch results for '{book_name}':")
        found_books = [book for book in self.inventory if book_name.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(f"{book.title} by {book.author} ({book.publication_year})")
        else:
            print(f"No books found with the title '{book_name}'.")

    def status(self, book_name):
        for book in self.inventory:
            if book.title == book_name:
                status = "available" if book.availability else "checked out"
                print(f"{book.title} is {status}.")
                return
        print(f"Book not found: {book_name}")

library = Library()

library.add("The Hobbit", "J.R.R. Tolkien", 1937)
library.add("To Kill a Mockingbird", "Harper Lee", 1960)
library.add("1984", "George Orwell", 1949)

library.available_books()

library.remove("To Kill a Mockingbird")

library.available_books()

library.search("the")

library.status("The Hobbit")
