#Weston Culpepper
#11/10/24
#Comp163-012
#This is the main portion of the code where it takes an input for the inventory file then displays a menu
#The user picks an option on the menu displayed, and it outputs all the books in that genre formatted

#imports needed packages and make inventory dictionary
import csv
from Book import Book
from Author import Author
inventory = {}

#displays a menu for the user of all the genres available
def displayMenu(options):
    while True:
        for idx, genre in enumerate(options):
            print(f'{idx+1}) {genre}')
        print(f'{len(options)+1}) Exit')
        genreOption = int(input('Enter your choice: '))
        if genreOption == len(options)+1:
            print('\nAggie Book Store\nGood Bye')
            return None
        elif 1 <= genreOption <= len(options):
            return genreOption - 1
        else:
            print("Invalid choice. Please try again.")

#displays the formatted genre inventory based on the choice made above in the displayMenu function
def displayGenreInv(genreOption, booksList=None):
    if genreOption is None:
        return

    genres = list(inventory.keys())
    if booksList:
        selected_books = booksList
    elif 0 <= genreOption < len(genres):
        genre = genres[genreOption]
        print(f"{genre}")
        selected_books = inventory.get(genre, [])
    else:
        print("Invalid genre selection.")
        return

    total = 0
    total_cost = 0

    print(f'\t{'Author':<19} {'Title':<29} {'Published':<9} {'QTY':<4} {'Price':<5}', end='\n')
    for book in selected_books:
        price = book.price if isinstance(book.price, (int, float)) else 0.0
        qty = book.getQuantity() if isinstance(book.getQuantity(), int) else 0
        price_display = f"{price:.1f}" if price.is_integer() else f"{price:.2f}"
        print(f"\t{book.author.getName():<19} {book.title:<29} {'2024':<9} {qty:<4} {price_display:<20}", end = '\n')
        total+=qty
        total_cost+= price * qty
    print(f'\t{"=" * 33}')
    print(f'\tInventory count {total} : Total ${total_cost:.2f}')



#reads the inventory file and stores it into a list, outputs the list
def readInv(file):
    global inventory
    booksList = []
    try:
        with open(file,'r') as inventory_file:
            reader = csv.reader(inventory_file)

            for row in reader:
                genre, fname, mname, lname, title, dob, year, price, qty, ISBN = row
                author = Author(fname, mname, lname, dob)
                try:
                    price = float(price)
                    qty = int(qty)
                    year = int(year)

                except ValueError:
                    print(f"Skipping row due to invalid data types: {row}")
                    continue

                book = Book(genre, title, author, price, qty, ISBN, year)
                booksList.append(book)

                if genre not in inventory:
                    inventory[genre] = []
                inventory[genre].append(book)

    except FileNotFoundError:
        print(f"File {file} not found. Please ensure it exists.")
    except Exception as e:
        print(f"An error occurred while loading the inventory: {e}")

    return booksList

#runs all the pieces of code
def main():
    inv_file = input('Enter inventory file: ')
    readInv(inv_file)

    genres = list(inventory.keys())
    while True:
        genreOption = displayMenu(genres)
        if genreOption is None:
            break
        displayGenreInv(genreOption)

#calls main function
main()
