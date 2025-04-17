# completare l'esercizio pag 128-129
import book
import library as lib


def main():
    test_book = book.Book("Rush", "Lewis", "98991122")
    test_lib = lib.Library(test_book)
    test_book.add_new_book()
    test_lib.show_catalog()
    







if __name__ == '__main__':
    main()