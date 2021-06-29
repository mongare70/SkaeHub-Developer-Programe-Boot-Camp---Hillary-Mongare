import unittest
import leap_year_tester

class TestLeapYearTester(unittest.TestCase):
    
    # test if leap year
    def test_leap_year_true(self):
        self.assertTrue(leap_year_tester.leap_year_tester(2000))
        self.assertTrue(leap_year_tester.leap_year_tester(2400))

    # test if not leap year
    def test_leap_year_false(self):
        self.assertFalse(leap_year_tester.leap_year_tester(1800))
        self.assertFalse(leap_year_tester.leap_year_tester(1900))
        self.assertFalse(leap_year_tester.leap_year_tester(2100))
        self.assertFalse(leap_year_tester.leap_year_tester(2200))
        self.assertFalse(leap_year_tester.leap_year_tester(2300))
        self.assertFalse(leap_year_tester.leap_year_tester(2500))

    # test if correct type
    def test_if_correct_type(self):
        with self.assertRaises(TypeError):
            leap_year_tester.leap_year_tester("")


if __name__ == '__main__':
    unittest.main()