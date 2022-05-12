import unittest
from game import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.p1 = Game('paper', 1)
        self.p2 = Game('rock', 1)
        self.p3 = Game('scissor', 1)
        self.r1 = Game('paper', 2)
        self.r2 = Game('rock', 2)
        self.r3 = Game('scissor', 2)
        self.s1 = Game('paper', 3)
        self.s2 = Game('rock', 3)
        self.s3 = Game('scissor', 3)
        self.int_check = Game(3, None)
        self.float_check = Game(5.4, None)
        self.wrong_str = Game('', None)

    def tearDown(self):
        del self.p1
        del self.p2
        del self.p3
        del self.r1
        del self.r2
        del self.r3
        del self.s1
        del self.s2
        del self.s3
        del self.int_check
        del self.float_check
        del self.wrong_str

    def test_init(self):

        self.assertEqual(self.p1.__str__(), 'Computer is paper. You are paper. You tie')
        self.assertEqual(self.p2.__str__(), 'Computer is paper. You are rock. You lose')
        self.assertEqual(self.p3.__str__(), 'Computer is paper. You are scissor. You win')
        self.assertEqual(self.r1.__str__(), 'Computer is rock. You are paper. You win')
        self.assertEqual(self.r2.__str__(), 'Computer is rock. You are rock. You tie')
        self.assertEqual(self.r3.__str__(), 'Computer is rock. You are scissor. You lose')
        self.assertEqual(self.s1.__str__(), 'Computer is scissor. You are paper. You lose')
        self.assertEqual(self.s2.__str__(), 'Computer is scissor. You are rock. You win')
        self.assertEqual(self.s3.__str__(), 'Computer is scissor. You are scissor. You tie')

        with self.assertRaises(TypeError):
            self.int_check.__str__()
        with self.assertRaises(TypeError):
            self.float_check.__str__()
        with self.assertRaises(ValueError):
            self.wrong_str.__str__()


if __name__ == '__main__':
    unittest.main()
