import unittest
import length_of_last_word

class TestLengthOfLastWord(unittest.TestCase):
    
    # blank input test 
    def test_blant_input(self):
        self.assertEqual(length_of_last_word.length_of_last_word(""), 0)

    # multiple words with whitespace test
    def test_multiple_words(self):
        self.assertEqual(length_of_last_word.length_of_last_word("Hello world!"), 6)

    # one-word input test
    def test_one_word(self):
        self.assertEqual(length_of_last_word.length_of_last_word("Hello"), 5)

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(TypeError):
            length_of_last_word(66)
    
    
if __name__ == '__main__':
    unittest.main()