


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.mulitiply import *

class TestMultiply(unittest.TestCase):

    def test_value_0(self):
        a=3
        b=2
        self.assertEqual(multiply(a,b), a*b)

def suite():
    suite = unittest.makeSuite(TestMultiply, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())















if __name__ == "__main__":
    run()