from esercizio2 import Book

        
class Library:
    """Libtary represents a real library creating books"""
    def __init__(self):
        self.books_catalog = []
    
    def create(self, my_title: str, my_author: str, my_pages: int) -> str:
        
        my_book = Book(my_title, my_author, my_pages)
        self.books_catalog.append(my_book)
        return f"{my_book} successfully added to {self.books_catalog}"
    
    def update(self, new_book: Book, old_book: Book):
        if new_book == old_book:
            return f"{new_book} is already on the catalog"
        else:
            if new_book in self.books_catalog:
                pass #@todo
    
    def delete(self, book_to_remove: Book):
        if book_to_remove in self.book_to_remove:
            pass # @todo
    
    def view():
        pass # @todo
        
        
            
def main():
    pass

if __name__ == '__main__':
    main()