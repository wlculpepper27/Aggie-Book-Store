#Weston Culpepper
#11/10/24
#Comp163-012
#Makes a class for book, constructor and methods(Inherits from Item class)

#imports Item class from Item file
from Item import Item
from Author import Author

class Book(Item, Author):
#constructor
    def __init__(self, genre, title, author, price, qty, ISBN, year):
        Item.__init__(self,'Book', price, qty)
        self.genre = genre
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.year = year

#getter methods
    def getGenre(self):
        return self.genre

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author.getName()

    def getISBN(self):
        return self.ISBN

    def getYear(self):
        return self.year
