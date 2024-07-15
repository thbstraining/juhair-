import unittest
from dataprocessing.book_data import BookData

class TestBookData(unittest.TestCase):
    def setUp(self):
        self.book_data = BookData()

    def test_add_and_get_book(self):
        self.book_data.add_book("Book Title", "Fiction", "Author Name")
        book = self.book_data.get_book("Book Title")
        self.assertEqual(book, {'genre': 'Fiction', 'author': 'Author Name'})

    def test_add_and_get_author(self):
        self.book_data.add_author("Author Name", "Author Biography")
        author = self.book_data.get_author("Author Name")
        self.assertEqual(author, {'biography': 'Author Biography'})

    def test_save_and_load_books(self):
        self.book_data.add_book("Book Title", "Fiction", "Author Name")
        self.book_data.save_books("test_books.json")
        new_book_data = BookData()
        new_book_data.load_books("test_books.json")
        book = new_book_data.get_book("Book Title")
        self.assertEqual(book, {'genre': 'Fiction', 'author': 'Author Name'})

if __name__ == '__main__':
    unittest.main()
