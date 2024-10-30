import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fx_convertor import swap_currency

class  TestSwapCurrency(unittest.TestCase):

    def setUp(self):
        # default fx data to designed test results
        self.spot_rate = {
            'EUR': 1.0, 
            'USD': 1.08, 
            'GBP': 0.83, 
            'JPY': 163.22,
            'PNL': 4.34
        }
    
    
    def tearDown(self):
        pass
    
    def test_convert_usd_to_gbp(self, amount:float = 100):
        print(f'hello Wiola,Twoja kwota: {amount}')
        print(self.spot_rate['PNL'])
        result = swap_currency(amount, self.spot_rate['PNL'], self.spot_rate['GBP'])
        self.assertAlmostEqual(result, 19.12, 2)

if __name__ =='__main__':
    unittest.main()