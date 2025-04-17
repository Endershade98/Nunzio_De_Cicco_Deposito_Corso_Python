import book

class Library:
    
    def __init__(self, book: book.Book):
        self.book = book
        self.catalog = []
    
    def add_book(self):
        self.catalog.append(self.book)
        return f"{self.book} successfully added"
    
    def remove_book(self, isbn):
        if self.book.isbn == isbn:
            self.catalog.remove(self.book)
            return f"{self.book} successfully removed"
    
    def search_title(self, title):
        listed_books = []
        if self.book.title == title:
            for self.book in self.catalog:
                listed_books.append(self.book)
            return f"books with same title {title}, successfully added to {listed_books}"
    
    def show_catalog(self):
        for book in self.catalog:
            return book.describe()
                    
                
    
    