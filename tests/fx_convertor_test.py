import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fx_convertor import swap_currency




class  TestSwapCurrency(unittest.TestCase):

    def setUp(self):
        self.spot_rate = {
            'EUR': 1.0, 
            'USD': 1.08, 
            'GBP': 0.83, 
            'JPY': 163.22
        }
        self.user_currency: str = "USD"
        self.user_given_amount: float = 100
        self.swap_currency: str = 'GBP'
    
    def test_convert_usd_to_gbp(self):
        result = swap_currency(self.spot_rate[self.user_currency], 100, self[swap_currency])
        self.assertAlmostEqual(result, 76.85)

if __name__ =='__main__':
    unittest.main()