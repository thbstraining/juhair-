from collections import Counter

def analyze_genre_popularity(books):
    genres = [book['genre'] for book in books.values()]
    return dict(Counter(genres))

def analyze_author_popularity(books):
    authors = [book['author'] for book in books.values()]
    return dict(Counter(authors))
