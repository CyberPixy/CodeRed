import unittest
import datetime

today = datetime.datetime.now()
class TestFetchAndSave(unittest.TestCase):
    
    def setUp(self):
        print(f'Test ready...{today}')
        # self.today_date = datetime.today()
       

    def test_get_date_one_year_ago(self):
        print("Ready to test from_date: ..")
        result = today.replace(month=today.month -1).strftime('%Y-%m-%d')
        # self.assertEqual(result, today.strftime('%Y-%m-%d'))
        print(result)



if __name__ == '__main__':
    unittest.main()