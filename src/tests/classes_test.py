import unittest
from classes import Database_Interactions, User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_registering_successful(self):
        self.assertEqual(self.user.register("testaus", "testaus"), True)
        self.user.deleteuser("testaus", "testaus")

    #def test_registering_unsuccessful(self):

    def test_deletinguser_successful(self):
        self.user.register("testaus", "testaus")
        self.assertEqual(self.user.deleteuser("testaus", "testaus"), True)

    #def test_deletinguser_unsuccessful_no_user_found(self):

    #def test_deletinguser_unsuccessful_password_wrong(self):

class TestDatabase_interactions(unittest.TestCase):
    def setUp(self):
        self.db = Database_Interactions()

    def test_adding_to_database_unsuccessful(self):
        self.assertEqual(self.db.addinfofromfile(1,"eitoimi.txt"), None)