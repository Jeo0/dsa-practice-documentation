"""
Hands-On Activity 1: Creating and Using a Class in Python
Objective:

Understand how to define a class, create objects, and access class attributes and methods.
Instructions:

    Define a class named Book with the following attributes:
        title (public)
        author (public)
        __price (private)

    Create a constructor that takes all three attributes as input when creating a new object.

    Create a public method get_price() to access the private __price attribute.

    Create another public method display_info() to print the book’s title, author, and price.

    Create two objects of the Book class and call the display_info() method for both.

SUBMIT THE FOLLOWING:
Screen Capture of your code and output.
"""


class Book:
    def __init__(self, title = None, author = None, price = 0):
        self.title = title
        self.author = author
        self.__price__ = price

    def get_price(self) -> int:
        return self.__price__
    
    def display_info(self) -> None:
        print("title: {:>3}".format(self.title))
        print("author: {:>3}".format(self.author))
        print("price: {:>3}".format(self.get_price()))


if __name__ == "__main__":
    capstone = Book(author="jise", title="Capstone Projik", price=123)
    capstone.display_info()

    print("\n\n")

    fictionko = Book("Hanataan", "JIJISI", 909090)
    fictionko.display_info()
