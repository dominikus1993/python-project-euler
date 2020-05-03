import unittest
import euler3

class TestProjectEuler(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(euler3.solve(600851475143), 6857)



if __name__ == '__main__':
    unittest.main()