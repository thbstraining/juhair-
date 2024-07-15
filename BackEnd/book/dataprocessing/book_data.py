import json

class BookData:
    def __init__(self):
        self.books = {}
        self.authors = {}

    def add_book(self, title, genre, author):
        self.books[title] = {'genre': genre, 'author': author}

    def add_author(self, name, biography):
        self.authors[name] = {'biography': biography}

    def get_book(self, title):
        return self.books.get(title)

    def get_author(self, name):
        return self.authors.get(name)

    def save_books(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.books, file)

    def load_books(self, file_path):
        with open(file_path, 'r') as file:
            self.books = json.load(file)
