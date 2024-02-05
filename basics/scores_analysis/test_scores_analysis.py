# test_scores_analysis.py
import pytest
from scores_analysis import analyze_scores


def test_scores_analysis():
    test_scores = [75, 88, 92, 67, 85, 94, 70, 79]
    highest, lowest, average = analyze_scores(test_scores)
    assert highest == 94
    assert lowest == 67
    assert round(average, 2) == 81.25


if __name__ == '__main__':
    pytest.main()
