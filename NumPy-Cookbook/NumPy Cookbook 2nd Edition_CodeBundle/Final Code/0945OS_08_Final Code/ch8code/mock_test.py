from __future__ import print_function
from mock import MagicMock
import numpy as np
import unittest

class NuclearReactor():
   def __init__(self, n):
      self.n = n

   def do_work(self, msg):
      print("Working")

      return self.factorial(self.n, msg)

   def factorial(self, n, msg):
      print(msg)

      if n == 0:
         return 1

      if n < 0:
         raise ValueError, "Core meltdown"

      return np.arange(1, n+1).cumprod()

class NuclearReactorTest(unittest.TestCase):
   def test_called(self):
      reactor = NuclearReactor(3)
      reactor.factorial = MagicMock(return_value=6)
      result = reactor.do_work("mocked")
      self.assertEqual(6, result)
      reactor.factorial.assert_called_with(3, "mocked")

   def test_unmocked(self):
      reactor = NuclearReactor(3)
      reactor.factorial(3, "unmocked")
      np.testing.assert_raises(ValueError)

if __name__ == '__main__':
    unittest.main()
