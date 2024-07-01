# Modularization - separating functionality into separate files
# separates concerns and organize our code into "categories" 

# managing individual instances of a book
# what are some attributes a book could have
# what are some methods i may need for a book
# how are those methods going to interact with my book attributes
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # managing if the book is available to check out
        self.is_available = True #setting a default attribute
    
    # method for checking out a book
    # check if is_available is equal to True
    def check_out(self):
        # check if is_available is True
        if self.is_available:
            # if it is, we set it to False
            # because we can consider this book checked out
            self.is_available = False
            # return True because we will use this function to see if we can succesfully check out a book object
            return True
        return False
    
    def return_book(self):
        # returns our book so we set self.is_available back to True
        self.is_available = True

# this is for the import example but not a necessary part of the library example  
publisher = "Penguin Books"


# driver code for the libary management system
from library import Library
from book import Book

def main():
    # instantiates a library object
    library = Library() #even if the class doesnt take any arguments for the init, you always need parentheses

    while True:
        action = input("What would you like to do: (add, lend, return, search, exit) （。＾▽＾）")
        if action == "exit":
            break
        try: 
            if action == "add":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                # instantiate our book class to create a book object
                new_book = Book(title, author)
                # calls the library add_book method to add the book object to library.books -> self.books
                library.add_book(new_book)
                print(f"Added book: {title}")
            elif action == "lend":
                title = input("Which book would you like to lend? ")
                library.lend_book(title)
            
            elif action == "return":
                title = input("Enter book title to return: ")
                library.return_book(title)
            elif action == "search":
                title = input("Which would you like to search for? ")
                book = library.find_book(title)
                if book:
                    availability = "available" if book.is_available else "not available"
                    print(f"{title} by {book.author} is {availability}")
                else:
                    print(f"{title} not found")
        except Exception as e:
            print(f"An error occurred: {e}")

main()