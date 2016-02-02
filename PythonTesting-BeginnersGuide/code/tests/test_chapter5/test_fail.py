from unittest import TestCase, main

class test_with_fail(TestCase):
    def test_less_than(self):
        if not (2.3 < 5.6):
            self.fail('2.3 is not less than 5.6, but it should be')

if __name__ == '__main__':
    main()

