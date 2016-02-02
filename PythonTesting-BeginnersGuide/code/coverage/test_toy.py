from unittest import TestCase
import toy


class test_global_function(TestCase):
    def test_positive(self):
        self.assertEqual(toy.global_function(3), 4)

    def test_negative(self):
        self.assertEqual(toy.global_function(-3), -2)

    def test_large(self):
        self.assertEqual(toy.global_function(2 ** 13), 2 ** 13 + 1)


class test_example_class(TestCase):
    def test_timestwo(self):
        example = toy.example_class(5)
        self.assertEqual(example.timestwo(), 10)
