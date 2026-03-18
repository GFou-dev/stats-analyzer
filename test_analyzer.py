from analyzer import mean, median, left_quarter, right_quarter, remove_outliers, interquartile_range, mode, variance, standard_deviation, z_score, mean_absolute_deviation
import pytest


def test_mean():
    assert mean([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5


def test_median():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 3, 4, 5]) == 3


def test_left_quarter():
    assert left_quarter([1, 2, 3, 4]) == 1.5
    assert left_quarter([1, 2, 3, 4, 5]) == 1.5
    assert left_quarter([1, 2, 3, 4, 5, 6]) == 2
    assert left_quarter([1, 2, 3, 4, 5, 6, 7]) == 2


def test_right_quarter():
    assert right_quarter([1, 2, 3, 4]) == 3.5
    assert right_quarter([1, 2, 3, 4, 5]) == 4.5
    assert right_quarter([1, 2, 3, 4, 5, 6]) == 5
    assert right_quarter([1, 2, 3, 4, 5, 6, 7]) == 6


def test_remove_outliers():
    assert remove_outliers([1, 10, 10, 11, 11, 12, 13]) == [10, 10, 11, 11, 12, 13]
    assert remove_outliers([9, 10, 11, 12]) == [9, 10, 11, 12]


def test_interquartile_range():
    assert interquartile_range([1, 2, 3, 4]) == 2
    assert interquartile_range([1, 2, 3, 4, 5, 6]) == 3
    assert interquartile_range([1, 2, 3, 4, 5, 6, 7]) == 4


def test_mode():
    assert mode([1, 1, 2, 3, 4]) == ([1], 2)
    assert mode([1, 2, 3, 4]) == ("No mode", 0)


def test_variance():
    assert variance([1, 2, 3, 4, 5, 6]) == 2.9167
    assert variance([1, 2, 3, 4, 5, 6], sample=True) == 3.5
    assert variance([12, 12, 12, 12]) == 0


def test_standard_deviation():
    assert standard_deviation([1, 2, 3, 4, 5, 6]) == 1.7078
    assert standard_deviation([1, 2, 3, 4, 5, 6], sample=True) == 1.8708
    assert standard_deviation([12, 12, 12, 12]) == 0


def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
    assert mean_absolute_deviation([1, 1, 1, 1]) == 0


def test_z_score():
    assert z_score([1, 2, 3, 4, 5, 6]) == [-1.46, -0.88, -0.29, 0.29, 0.88, 1.46]
    assert z_score([12, 12, 12, 12]) == None

