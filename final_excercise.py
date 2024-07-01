from library import book
from library import Library
from book import Book
# Further expand you character class
# Create a class to manage your characters
# give that class the option to add a character
# and display each character


# Create a new attribute on your character to manage a collection of inventory objects
library = Library()
book = Book("LOTR", "Author")
library.add_book(book)

# example for displaying all books
for book in library.books:
    print(book.title)