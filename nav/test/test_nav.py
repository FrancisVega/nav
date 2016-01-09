import sys
sys.path.append('/repos/nav')

import unittest
from nav import *

class Demo(unittest.TestCase):

    def setUp(self):
        pass


    def test_directoryExists(self):
        dir = "/Users/hisco"
        print dirExists(dir)



if __name__ == '__main__':
    unittest.main()
