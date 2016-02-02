from unittest import main
from mocker import MockerTestCase
from time import time

class test_mocker_integration(MockerTestCase):
    def test_mocking_context(self):
        mocker = self.mocker
        time_mock = mocker.replace('time.time')
        time_mock()
        mocker.result(1.0)

        mocker.replay()

        self.assertAlmostEqual(time(), 1.0)

if __name__ == '__main__':
    main()
