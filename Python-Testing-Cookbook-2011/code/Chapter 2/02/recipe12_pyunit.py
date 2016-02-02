if __name__ == "__main__":
    import unittest
    from recipe12 import *
    suite = unittest.TestLoader().loadTestsFromTestCase(\
                                        ShoppingCartTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
