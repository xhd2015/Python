from unittest import TestCase, main

class floating_point_problems(TestCase):
    def test_assertEqual(self):
        self.assertEqual((7.0 ** 0.5) ** 2.0, 7.0)

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual((7.0 ** 0.5) ** 2.0, 7.0)

if __name__ == '__main__':
    main()

