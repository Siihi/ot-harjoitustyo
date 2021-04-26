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

    #def test_login_successful(self):

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
        self.assertEqual(self.db.addinfofromfile(1,"eitoimi.txt"), None)

    def test_adding_to_database_successfully(self):
        self.assertEqual(self.db.addinfofromfile(1, "testi.csv"), True)

    def test_fetching_all_info(self):
        self.assertEqual(self.db.fetchallinfo(1), True)

    def test_addingcash_successful(self):
        self.assertEqual(self.db.addcash(1, "10,00"), True)

    def test_addingcash_unsuccessful(self):
        self.assertEqual(self.db.addcash(1, "3.0"), None)