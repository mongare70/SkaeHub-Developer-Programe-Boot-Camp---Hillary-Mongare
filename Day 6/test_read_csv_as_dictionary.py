import unittest
import read_csv_as_dictionary

class TestReadCsvAsDictionary(unittest.TestCase):
    
    # read csv test 
    def test_read_csv(self):
        self.assertIsNotNone(read_csv_as_dictionary.read("peeps.csv"))

    # file not found test
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_csv_as_dictionary.read("")

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(OSError):
            read_csv_as_dictionary.read(6)
    
    
if __name__ == '__main__':
    unittest.main()