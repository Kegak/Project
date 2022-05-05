import unittest
from game import *


class MyTestCase(unittest.TestCase):
    def test_all(self):
        """
        I have no clue how to test this properly because it has
        random values. So if eight of these tests fail and one
        passes then we're calling it good. :(
        """
        self.assertEqual(self.__str__(), 'Computer is paper. You are paper. You tie')
        self.assertEqual(self.__str__(), 'Computer is paper. You are rock. You lose')
        self.assertEqual(self.__str__(), 'Computer is paper. You are scissor. You win')
        self.assertEqual(self.__str__(), 'Computer is rock. You are paper. You win')
        self.assertEqual(self.__str__(), 'Computer is rock. You are rock. You tie')
        self.assertEqual(self.__str__(), 'Computer is rock. You are scissor. You lose')
        self.assertEqual(self.__str__(), 'Computer is scissor. You are paper. You lose')
        self.assertEqual(self.__str__(), 'Computer is scissor. You are rock. You win')
        self.assertEqual(self.__str__(), 'Computer is scissor. You are scissor. You tie')


if __name__ == '__main__':
    unittest.main()
