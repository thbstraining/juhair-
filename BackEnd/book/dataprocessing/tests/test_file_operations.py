import unittest
from dataprocessing.file_operations import save_data_to_file, load_data_from_file

class TestFileOperations(unittest.TestCase):
    def test_save_and_load_data(self):
        data = {'key': 'value'}
        file_path = 'test_data.json'
        save_data_to_file(data, file_path)
        loaded_data = load_data_from_file(file_path)
        self.assertEqual(data, loaded_data)

if __name__ == '__main__':
    unittest.main()
