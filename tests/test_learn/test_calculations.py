import unittest
import calculations



class TestCalc(unittest.TestCase):

    def test_1add(self):
        self.assertEqual(calculations.add(10,5), 15)
        self.assertEqual(calculations.add(-1, 1), 0)
        self.assertEqual(calculations.add(-2, -1), -3)
        self.assertEqual(calculations.add(0, 0),0)

    def test_substract(self):
        self.assertEqual(calculations.substract(10, 5), 5)
        self.assertEqual(calculations.substract(-1, 1), -2)
        self.assertEqual(calculations.add(-2, -1), -3)
        self.assertEqual(calculations.add(0, 0), 0)
    
    def test_divide(self):
        # with self.assertRaises(ZeroDivisionError):
        #     unit_testing.divide(10, 0)
        self.assertEqual(calculations.divide(10, 5), 2)
        self.assertEqual(calculations.divide(-1, 1), -1)
        self.assertEqual(calculations.divide(-2, -1), 2)
        self.assertEqual(calculations.divide(5, 2), 2.5)
        # two ways od dealing with zero value devider firts
        # self.assertRaises(ZeroDivisionError, calculations.divide, 10, 0)
        # second way
        with self.assertRaises(ValueError):
            calculations.divide(10, 0)




# run test 
if __name__ == "__main__":
    unittest.main()