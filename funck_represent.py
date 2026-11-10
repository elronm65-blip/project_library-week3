

books = [{        "id": 1,        "name": "Harry Potter",        "author": "J.K. Rowling",        "year": 1997,        "available": False    },    {        "id": 2,        "name": "The Hobbit",        "author": "J.R.R. Tolkien",        "year": 1937,        "available": True    },    {        "id": 3,        "name": "Clean Code",        "author": "Robert Martin",        "year": 2008,        "available": False    },    {        "id": 4,        "name": "Atomic Habits",        "author": "James Clear",        "year": 2018,        "available": True    },    {        "id": 5,        "name": "The Pragmatic Programmer",        "author": "David Thomas",        "year": 1999,        "available": False    }]

def display_books(books):
   for book in books:
      print(book)

def search_book(books, name):
    for book in books:     
      if name in book["name"]:
        return book
    return None  


def add_book(books, name, author, year):
    if year == 0:
        return "year canot be zero"
    if len(author) == 0:
        return "cannot append book without author"

    for book in books:
       if book["author"] == author and book["name"] == name:
            return 'this  book is already have in same author'
          
    
       
    new_book =  {"id": get_next_book_id(books),"name": name,"author":author,"year": year,"available": True}
    try:
        books.append(new_book)
        return True
    except:
       return False
      
   

def get_next_book_id(books):
   new_id = len(books) + 1
   return new_id

def borrow_book(books, book_id):
    if book_id > len(books):
        return "the id  book not in library"
    for book in books:
      if book["id"] == book_id:
        if book in get_available_books(books):
            book["available"] = False
            return True
    return 'cannot borrrow book because he is borrow already'   
        
def return_book(books, book_id):
    if book_id > len(books):
        return "the id  book not in library"
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                book["available"]  = True
                return True
            return "cannot return book that already exict"
          
def get_available_books(books):
    avilibale_books =[]
    for book in books:
      if book["available"] == True:
        avilibale_books.append(book)
    return avilibale_books    

def get_books_by_author(books, author):
    books_author = []
    for book in books:
        if book["author"] == author:
           books_author.append(book)
    return books_author       

