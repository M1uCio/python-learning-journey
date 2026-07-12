import json

playing = True

def LoadBooks():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No file found, creating a new one")
        return []

def SaveBooks(books):
    with open("library.json", "w") as file:
        json.dump(books, file, indent=4)

def AddBook():
    title = input("Insert the title of the book:")
    author = input("Insert the author of the book:")
    while True:
        try:
            year = int(input("Insert the year of release of this book:"))
            if year > 0:
                break
            else:
                print("You must insert a positive number")
        except ValueError:
            print("You must insert a number")

    books = LoadBooks()
    books.append({"title": title, "author": author, "year": year})
    SaveBooks(books)

def DeleteBook():
    title = input("Insert a title of the book you want to delete: ")
    books = LoadBooks()
    BooksDeleted = 0
    New_Books = []
    Deleted_Books = []
    for book in books:
        if title.strip().lower() not in book["title"].strip().lower():
            New_Books.append(book)
        else:
            BooksDeleted += 1
            Deleted_Books.append(book)
    SaveBooks(New_Books)
    if BooksDeleted > 0:
        print(f"{"-"*10}Deleted {BooksDeleted} books, here they are: ")
        for i, book in enumerate(Deleted_Books):
            print(f"{i+1}. {book["title"]}, {book["author"]}, {book["year"]} year")
    else:
        print(f"{"-"*10}No book to delete could be found.")


def SearchBook():
    BooksNumber = 0
    BooksList = []
    title = input("Insert the title of the book you want to search for: ")
    for book in LoadBooks():
        if title.strip().lower() in book["title"].strip().lower():
            BooksNumber += 1
            BooksList.append(book)
    if BooksNumber > 0:
        print(f"{"-"*10} {BooksNumber} books found, here they are: ")
        for i, book in enumerate(BooksList):
            print(f"{i+1}. {book["title"]}, {book["author"]}, {book["year"]} year")
    else:
        print(f"{"-"*10}No book could be found.")

def PrintBooks():
    print(f"{"-"*15}Here are all the books:")
    for i, book in enumerate(LoadBooks()):
        print(f"{i+1}. {book["title"]}, {book["author"]}, {book["year"]} year")

def PrintMenu():
    print(f"{'-'*15}What would you like to do?{'-'*15}")
    print("1. Add a book(A)")
    print("2. Delete a book(D)")
    print("3. Search for a book(S)")
    print("4. Print all books info(P)")
    print("5. Exit the program(E)")

def Main():
    PrintMenu()
    choice = input("Insert your choice: ").strip().upper()
    if choice in ("A", "1"):
        AddBook()
        return True
    elif choice in ("D", "2"):
        DeleteBook()
        return True
    elif choice in ("S", "3"):
        SearchBook()
        return True
    elif choice in ("P", "4"):
        PrintBooks()
        return True
    elif choice in ("E", "5"):
        return False
    else:
        print("You didn't insert a correct option, choose one of A/D/S/P/E")
        return True

while playing:
    playing = Main()