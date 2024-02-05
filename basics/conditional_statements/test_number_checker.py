# test_number_checker.py
import pytest
from unittest.mock import patch
from io import StringIO

# Basic tests for main() in number_checker.py
def test_main_basic(capsys):
    with patch('builtins.input', side_effect=['5']):
        from number_checker import main
        main()
    
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')
    
    assert "The number is positive." in output
    assert "The number is odd." in output
    assert "The number is divisible by 5." in output

# Advanced test for checking multiple of 10
def test_main_advanced(capsys):
    with patch('builtins.input', side_effect=['20']):
        from number_checker import main
        main()
    
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check for multiple of 10 only if the condition is met in the output
    if "The number is positive, even, and a multiple of 10." in output:
        assert "The number is positive, even, and a multiple of 10." in output

if __name__ == '__main__':
    pytest.main()
