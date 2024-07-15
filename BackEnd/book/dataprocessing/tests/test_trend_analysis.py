import unittest
from dataprocessing.trend_analysis import analyze_genre_popularity, analyze_author_popularity

class TestTrendAnalysis(unittest.TestCase):

    def setUp(self):
        """
        Set up the test data for the analysis functions.
        """
        self.books = {
            1: {'title': 'Book One', 'genre': 'Science Fiction', 'author': 'Author A'},
            2: {'title': 'Book Two', 'genre': 'Fantasy', 'author': 'Author B'},
            3: {'title': 'Book Three', 'genre': 'Science Fiction', 'author': 'Author A'},
            4: {'title': 'Book Four', 'genre': 'Fantasy', 'author': 'Author C'},
        }

    def test_analyze_genre_popularity(self):
        """
        Test the analyze_genre_popularity function.
        """
        result = analyze_genre_popularity(self.books)
        expected = {'Science Fiction': 2, 'Fantasy': 2}
        self.assertEqual(result, expected)

    def test_analyze_author_popularity(self):
        """
        Test the analyze_author_popularity function.
        """
        result = analyze_author_popularity(self.books)
        expected = {'Author A': 2, 'Author B': 1, 'Author C': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
