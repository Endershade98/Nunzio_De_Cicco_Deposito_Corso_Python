from esercizio2 import Book

        
class Library:
    """Libtary represents a real library creating books"""
    def __init__(self):
        self.books_catalog = []
    
    def create(self, my_title: str, my_author: str, my_pages: int) -> str:
        
        my_book = Book(my_title, my_author, my_pages)
        self.books_catalog.append()
        return str(my_book)
    
    def update():
        pass
    
    def delete():
        pass
            
    
Book1 = Library.create("I dolori del giovane Doggo", "Mirko", 500)
print(Book1)