import unittest
from . import test_gol

def gol_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_gol)
    return suite
