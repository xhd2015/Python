from unittest import TestCase, main
from mocker import Mocker

import pid

class test_pid_constructor(TestCase):
    def test_without_when(self):
        mocker = Mocker()
        mock_time = mocker.replace('time.time')
        mock_time()
        mocker.result(1.0)

        mocker.replay()

        controller = pid.PID(P = 0.5, I = 0.5, D = 0.5,
                             setpoint = 0, initial = 12)

        mocker.restore()
        mocker.verify()

        self.assertEqual(controller.gains, (0.5, 0.5, 0.5))
        self.assertAlmostEqual(controller.setpoint[0], 0.0)
        self.assertEqual(len(controller.setpoint), 1)
        self.assertAlmostEqual(controller.previous_time, 1.0)
        self.assertAlmostEqual(controller.previous_error, -12.0)
        self.assertAlmostEqual(controller.integrated_error, 0)

    def test_with_when(self):
        controller = pid.PID(P = 0.5, I = 0.5, D = 0.5,
                             setpoint = 1, initial = 12,
                             when = 43)

        self.assertEqual(controller.gains, (0.5, 0.5, 0.5))
        self.assertAlmostEqual(controller.setpoint[0], 1.0)
        self.assertEqual(len(controller.setpoint), 1)
        self.assertAlmostEqual(controller.previous_time, 43.0)
        self.assertAlmostEqual(controller.previous_error, -11.0)
        self.assertAlmostEqual(controller.integrated_error, 0)

class test_calculate_response(TestCase):
    def test_without_when(self):
        mocker = Mocker()
        mock_time = mocker.replace('time.time')
        mock_time()
        mocker.result(1.0)
        mock_time()
        mocker.result(2.0)
        mock_time()
        mocker.result(3.0)
        mock_time()
        mocker.result(4.0)
        mock_time()
        mocker.result(5.0)

        mocker.replay()

        controller = pid.PID(P = 0.5, I = 0.5, D = 0.5,
                             setpoint = 0, initial = 12)

        self.assertEqual(controller.calculate_response(6), -3)
        self.assertEqual(controller.calculate_response(3), -4.5)
        self.assertEqual(controller.calculate_response(-1.5), -0.75)
        self.assertEqual(controller.calculate_response(-2.25), -1.125)

        mocker.restore()
        mocker.verify()

    def test_with_when(self):
        controller = pid.PID(P = 0.5, I = 0.5, D = 0.5,
                             setpoint = 0, initial = 12,
                             when = 1)

        self.assertEqual(controller.calculate_response(6, 2), -3)
        self.assertEqual(controller.calculate_response(3, 3), -4.5)
        self.assertEqual(controller.calculate_response(-1.5, 4), -0.75)
        self.assertEqual(controller.calculate_response(-2.25, 5), -1.125)


if __name__ == '__main__':
    main()

