import pytest
from program import ListManipulation


def test_comparison_of_averages_the_first_one_is_more(capfd):
    list_one = [1, 2, 3]
    list_two = [3, 3, 2]

    ListManipulation(list_two, list_one).comparison_of_averages()
    captured = capfd.readouterr()

    assert captured.out == 'Первый список имеет большее среднее значение\n'


def test_comparison_of_averages_the_second_one_is_more(capfd):
    list_one = [1, 2, 3]
    list_two = [3, 3, 2]

    ListManipulation(list_one, list_two).comparison_of_averages()
    captured = capfd.readouterr()

    assert captured.out == 'Второй список имеет большее среднее значение\n'


def test_comparison_of_averages_both_are_equal(capfd):
    list_two = [3, 3, 2]

    ListManipulation(list_two, list_two).comparison_of_averages()
    captured = capfd.readouterr()

    assert captured.out == 'Средние значения равны\n'


if __name__ == '__main__':
    pytest.main(['-v'])
