import unittest
import euler1

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler1.solve(), 233168)



if __name__ == '__main__':
    print(euler1.solve())
    unittest.main()