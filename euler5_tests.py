import unittest
import euler5

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler5.solve(), 232792560)



if __name__ == '__main__':
    unittest.main()