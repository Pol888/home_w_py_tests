import unittest
import sys
from program import ListManipulation


class TestListManipulation(unittest.TestCase):

    def setUp(self):
        self.ConsoleInterceptor = type("ConsoleInterceptor", (object,), {"__init__": lambda self: setattr(
            self, "messages", []), "write": lambda self, message: self.messages.append(message), "getvalue":
                                            lambda self: ''.join(self.messages), "flush": lambda self: None})
        self.interceptor = self.ConsoleInterceptor()
        sys.stdout = self.interceptor
        self.lists_for_the_test = [[1, 2, 3], [3, 3, 2], [3, 2, 3]]

    def test_comparison_of_averages_the_first_one_is_more(self):
        ListManipulation(self.lists_for_the_test[1], self.lists_for_the_test[0]).comparison_of_averages()
        self.assertEqual(self.interceptor.messages[0], 'Первый список имеет большее среднее значение')

    def test_comparison_of_averages_the_second_one_is_more(self):
        ListManipulation(self.lists_for_the_test[0], self.lists_for_the_test[1]).comparison_of_averages()
        self.assertEqual(self.interceptor.messages[0], 'Второй список имеет большее среднее значение')

    def test_comparison_of_averages_both_are_equal(self):
        ListManipulation(self.lists_for_the_test[1], self.lists_for_the_test[2]).comparison_of_averages()
        self.assertEqual(self.interceptor.messages[0], 'Средние значения равны')

    if __name__ == '__main__':
        unittest.main()
