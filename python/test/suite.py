import unittest, sys, os
sys.path.insert(0, '.')

from tickertest import *
from talibtest import *

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TickerTest))
    suite.addTest(unittest.makeSuite(TA_LIB_Test))
    unittest.TextTestRunner(verbosity=2).run(suite)
