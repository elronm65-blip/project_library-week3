from func_uteels import represition
from funck_represent import borrow_book ,return_book ,  display_books , search_book , add_book ,get_books_by_author , get_available_books


books = [    {        "id": 1,        "name": "Harry Potter",        "author": "J.K. Rowling",        "year": 1997,        "available": True    },    {        "id": 2,        "name": "The Hobbit",        "author": "J.R.R. Tolkien",        "year": 1937,        "available": True    },    {        "id": 3,        "name": "Clean Code",        "author": "Robert Martin",        "year": 2008,        "available": False    },    {        "id": 4,        "name": "Atomic Habits",        "author": "James Clear",        "year": 2018,        "available": True    },    {        "id": 5,        "name": "The Pragmatic Programmer",        "author": "David Thomas",        "year": 1999,        "available": False    }]

while True:

    print("""================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:""")
    choises={1,2,3,4,5,6,7,8}
    try:
        choise = int(input("chosse  from 1 - 0"))
    except ValueError:
        print("enter a number not a string")
        continue

    if choise not in choises:
        print("invalid choise")
        continue

    if choise == 1:
        display_books(books)
    if choise == 2: 
        name_book =input("chooose name of book")
        val = search_book(books, name_book)
        print(represition(val))
    if choise == 3:
        name = input("choose name")
        author = input ("choose author")
        year = int(input("choose year"))
        val = add_book(books, name, author, year)
        print(represition(val))
        
    if choise == 4 :
        book_id =int(input("choose id of book to borrow"))
        val = borrow_book(books, book_id)
        print(represition(val))

    if choise == 5:
        book_id = int(input("choose id of book to return"))
        val =return_book(books, book_id)
        print(represition(val))

    if choise == 6:
        val = get_available_books(books)
        print(represition(val))
    if choise == 7:
        author = input("choose author of book to search")
        val =get_books_by_author(books, author)
        print(represition(val))
       

    if choise == 8:
        break