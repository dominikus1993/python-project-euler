import unittest
import euler6

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler6.solve(), 25164150)



if __name__ == '__main__':
    unittest.main()