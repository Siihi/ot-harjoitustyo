import unittest
from classes import Database_Interactions, User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_login_no_user_found(self):
        self.assertEqual(self.user.login("testaus", "testaus"), False)

    def test_login_password_wrong(self):
        self.user.register("testaus", "testaus")
        self.assertEqual(self.user.login("testaus", "eitestaus"), False)
        self.user.deleteuser("testaus", "testaus")

    def test_login_successful(self):
        self.assertEqual(self.user.login("testi", "testi"), 1)

    def test_registering_successful(self):
        self.assertEqual(self.user.register("testaus", "testaus"), True)
        self.user.deleteuser("testaus", "testaus")

    def test_registering_unsuccessful(self):
        self.user.register("testaus", "testaus")
        self.assertEqual(self.user.register("testaus", "testaus"), False)
        self.user.deleteuser("testaus", "testaus")

    def test_deletinguser_successful(self):
        self.user.register("testaus", "testaus")
        self.assertEqual(self.user.deleteuser("testaus", "testaus"), True)

    def test_deletinguser_unsuccessful_no_user_found(self):
        self.assertEqual(self.user.deleteuser("testaus", "testaus"), False)

    def test_deletinguser_unsuccessful_password_wrong(self):
        self.user.register("testaus", "testaus")
        self.assertEqual(self.user.deleteuser("testaus", "eitestaus"), False)
        self.user.deleteuser("testaus", "testaus")

class TestDatabase_interactions(unittest.TestCase):
    def setUp(self):
        self.db = Database_Interactions()

    def test_adding_to_database_unsuccessful(self):
        self.assertEqual(self.db.addinfofromfile(1,"eitoimi.txt"), False)

    def test_adding_to_database_successfully(self):
        self.assertEqual(self.db.addinfofromfile(1, "testi.csv"), True)

    def test_fetching_all_info(self):
        self.assertEqual(self.db.fetchallinfo(-1), [])

    def test_addingcash_successful(self):
        self.assertEqual(self.db.addcash(1, "10,00"), True)

    def test_addingcash_unsuccessful(self):
        self.assertEqual(self.db.addcash(1, "3.0"), False)

    def test_addingcash_unsuccessful_not_int(self):
        self.assertEqual(self.db.addcash(1, "hehe,"), False)

    def test_adding_cash_purchase_successful(self):
        self.assertEqual(self.db.addcashpurchase(1, "-10,00", "Testi", "30.09.2000"), True)

    def test_adding_cash_purchase_unsuccessful(self):
        self.assertEqual(self.db.addcashpurchase(1, "0,30", "Testi", "2000"), False)

    def test_adding_cash_purchase_unsuccessful_not_int(self):
        self.assertEqual(self.db.addcashpurchase(1, "-hehe,", "testi", "30.09.2000"), False)

    def test_fetching_income_of_alltime(self):
        self.assertEqual(self.db.fetchincomeofalltime(-1), 0.0)

    def test_fetching_expenses_of_alltime(self):
        self.assertEqual(self.db.fetchexpensesofalltime(-1), 0.0)

    def test_fetching_income_of_month_successful(self):
        self.assertEqual(self.db.fetchincomeofmonth(1, "7", "1993"), 0.0)

    def test_fetching_expenses_of_month_successful(self):
        self.assertEqual(self.db.fetchexpensesofmonth(1, "7", "1993"), 0.0)