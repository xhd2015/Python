from unittest import TestCase, main

class two_failing_tests(TestCase):
    def test_assertTrue(self):
        self.assertTrue(1 == 1 + 1)

    def test_assertEqual(self):
        self.assertEqual(1, 1 + 1)

if __name__ == '__main__':
    main()

