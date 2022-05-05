import unittest
from game import *


class MyTestCase(unittest.TestCase):
    def test_paper(self):
        self.c_input = 1
        self.p_input = 'paper'
        self.assertEqual(__str__, 'Computer is paper. You are paper. You tie')


if __name__ == '__main__':
    unittest.main()
