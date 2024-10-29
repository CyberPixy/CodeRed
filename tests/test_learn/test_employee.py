import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
        
    def setUp(self):
    #    return super().setUp()
        print("setup")  #'''manifestation that setUp is runnig with all desigend test methods '''
        self.empl_2 = Employee('violeta', 'juszczyk', 3000)
        self.empl_3 = Employee('piotr', 'kodak', 25000)
    
    def tearDown(self):
        # eg create folder or file in data base
        pass

    def test_email(self):
        print("test_email")
        self.assertEqual(self.empl_2.email, 'violeta.juszczyk@email.com')
        self.assertEqual(self.empl_3.email, 'piotr.kodak@email.com')

    def test_fullname(self):
        print("test_full_name")
        self.assertEqual(self.empl_2.full_name,'violeta, Juszczyk')





if __name__ == '__main__':
    unittest.main()
