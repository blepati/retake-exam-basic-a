# Create a Book class, that has an author, a title and a release year
# Create a constructor for setting those values
# Book should be represented as string in this format:
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
# Create a BookShelf class that has a list of books in it
# We should be able to add and remove books.
# We should be able to query the favourite author (who has written the most books in the shelf)
# We should be able to query the earliest published books.
# We should be able to query the latest published books.
# Bookself should have a method whitch give us information about the number of books, the earliest and the latest released books, and the favourite author

class Book(object):
    def __init__(self):
        self.author = ""
        self.title = ""
        self.release_year = 0

    def __repr__(self):
        return self.author + ": " + self.title + " (" + str(self.release_year) +")"

class BookShelf(object):
    def __init__(self):
        self.list_of_books = []

    def books(self):
        books_in_shelf = len(self.list_of_books)
        if books_in_shelf == 0:
            return "You have no books here."
        if books_in_shelf > 0:
            return "You have " + str(books_in_shelf) + " books"

    def put(self, author, title, release_year):
        book = Book()
        book.author = author
        book.title = title
        book.release_year = release_year
        self.list_of_books.append(book)

    def remove(self, title):
        temp_list = []
        for book in  self.list_of_books:
            if book.title != title:
                temp_list.append(book)
        self.list_of_books = temp_list
        return self.list_of_books

my_shelf = BookShelf()
print(my_shelf.books())
 #Should print out:
 #You have no books here.

my_shelf.put("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
my_shelf.put("Douglas Adams", "Mostly Harmless", 1992)
my_shelf.put("Frank Herbert", "Dune", 1965)
my_shelf.put("Frank Herbert", "The Dragon in the Sea", 1957)
print(my_shelf.books())
my_shelf.remove("The Dragon in the Sea")
print(my_shelf.books())
# Should print out:
# You have 3 books.
# Earliest released: Frank Herbert : Dune (1965)
# Latest released: Douglas Adams : Mostly Harmless (1992)
# Favourite author: Douglas Adams
