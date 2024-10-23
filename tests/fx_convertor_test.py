import unittest
from src.fx_convertor import convert_currency

class  TestFXConvertor(unittest.TestCase):

    def setUp(self):
        self.spot_rate = {
            'EUR': 1.0, 
            'USD': 1.08, 
            'GBP': 0.83, 
            'JPY': 163.22
        }
    
    def test_convert_usd_to_GBP(self):
        result = convert_currency('USD', 'GBP', 100, self.spot_rate)
        self.assertAlmostEqual(result, 76.85)

if __name__ =='__main__':
    unittest.main()