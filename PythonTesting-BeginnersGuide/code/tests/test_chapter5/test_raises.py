from unittest import TestCase, main

class silly_int_test(TestCase):
    def test_int_from_string(self):
        self.assertRaises(ValueError, int, '8ca2', base = 16)

if __name__ == '__main__':
    main()

