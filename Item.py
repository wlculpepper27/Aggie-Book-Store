#Weston Culpepper
#11/10/24
#Comp163-012
#Makes a class for item, constructor and methods

class Item:
#constructor
    def __init__(self, item_type, price, quantity):
        self.item_type = item_type
        self.price = price
        self.quantity = quantity

#getter and setter methods
    def getType(self):
        return self.item_type

    def setType(self, item_type):
        self.item_type = item_type

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

