import unittest
from unittest.mock import patch
from grade_calculator import main

class TestGradeCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['80', '90', '70'])
    def test_grade_calculation(self):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Your final grade is: 82.0")

    # Additional test cases can be added here

if __name__ == '__main__':
    unittest.main()
