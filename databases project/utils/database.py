import DatabaseConnection

books=[]

def add_book(name, author):
    books.append({'name':name, 'author':author})

def read_book():
    return books

