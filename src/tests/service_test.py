import unittest
from services.service import Service, InvalidCredentialsError, UsernameExistsError

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    def test_current_user(self):
        self.assertEqual(self.service.current_user(), None)

    def test_login_successful(self):
        self.service.register("testaus", "testaus")
        self.assertEqual(self.service.login("testaus", "testaus"), None)
        self.service.deleteuser("testaus", "testaus")
    
    #def test_login_unsuccessful(self):

    def test_logout(self):
        self.assertEqual(self.service.logout(), None)

    def test_register_successful(self):
        self.assertEqual(self.service.register("testaus", "testaus"), None)
        self.service.deleteuser("testaus", "testaus")

    #def test_register_unsuccessful(self):

    def test_deleteuser_successful(self):
        self.service.register("testaus", "testaus")
        self.assertEqual(self.service.deleteuser("testaus", "testaus"), None)

    #def test_deleteuser_unsuccessful(self):

    def test_addinfo_successful(self):
        self.assertEqual(self.service.addinfo("testi.csv"), None)

    #def test_addinfo_unsuccessful(self):

    def test_addcash_successful(self):
        self.assertEqual(self.service.addcash("10,00"), None)

    #def test_addcash_unsuccessful(self):

    def test_addcashpurchase_successful(self):
        self.assertEqual(self.service.addcashpurchase("-10,00", "testi", "30.09.2000"), None)

    #def test_addcashpurchase_unsuccessful(self):

    def test_fetchallinfos(self):
        self.assertEqual(self.service.fetchallinfos(), [])

    def test_fetchincomeofalltime(self):
        self.assertEqual(self.service.fetchincomeofalltime(), 0.0)

    def test_fetchexpensesofalltime(self):
        self.assertEqual(self.service.fetchexpensesofalltime(), 0.0)

    def test_fetchincomeofmonth(self):
        self.assertEqual(self.service.fetchincomeofmonth(), 0.0)

    def test_fetchexpensesofmonth(self):
        self.assertEqual(self.service.fetchexpensesofmonth(), 0.0)