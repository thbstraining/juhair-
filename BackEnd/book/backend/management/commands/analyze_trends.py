# backend/management/commands/analyze_trends.py
from django.core.management.base import BaseCommand
from dataprocessing.trend_analysis import analyze_genre_popularity, analyze_author_popularity

class Command(BaseCommand):
    help = 'Analyze genre and author popularity from books data'

    def handle(self, *args, **options):
        # Sample data, replace this with actual data retrieval logic
        books = {
            1: {'title': 'Book One', 'genre': 'Science Fiction', 'author': 'Author A'},
            2: {'title': 'Book Two', 'genre': 'Fantasy', 'author': 'Author B'},
            3: {'title': 'Book Three', 'genre': 'Science Fiction', 'author': 'Author A'},
            4: {'title': 'Book Four', 'genre': 'Fantasy', 'author': 'Author C'},
        }

        genre_popularity = analyze_genre_popularity(books)
        author_popularity = analyze_author_popularity(books)

        self.stdout.write('Genre Popularity:')
        for genre, count in genre_popularity.items():
            self.stdout.write(f'{genre}: {count}')

        self.stdout.write('Author Popularity:')
        for author, count in author_popularity.items():
            self.stdout.write(f'{author}: {count}')
