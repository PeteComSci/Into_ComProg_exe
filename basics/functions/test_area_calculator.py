# test_area_calculator.py
import pytest
from area_calculator import calculate_area, calculate_perimeter

def test_calculate_area():
    assert calculate_area(5, 10) == 50
    assert calculate_area(7, 3) == 21
    # Add more test cases as needed

def test_calculate_perimeter():
    assert calculate_perimeter(5, 10) == 30
    assert calculate_perimeter(7, 3) == 20
    # Add more test cases as needed

if __name__ == '__main__':
    pytest.main()

