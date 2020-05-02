import unittest
import euler2

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler2.solve(), 4613732)



if __name__ == '__main__':
    unittest.main()