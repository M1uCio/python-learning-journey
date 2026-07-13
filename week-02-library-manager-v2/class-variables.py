from datetime import datetime

class Books:

    multiplier = 1.05
    num_of_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.price = int(50*(datetime.now().year - year))

        Books.num_of_books += 1

    def increase_price(self):
        self.price = int(self.price*self.multiplier)
        

book_1 = Books("The Hobbit", "J R R Tolkien", 1937)

print(book_1.price)

print(Books.num_of_books)