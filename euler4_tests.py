import unittest
import euler4

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler4.solve(), 906609)



if __name__ == '__main__':
    unittest.main()