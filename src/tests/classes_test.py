import unittest
from classes import Database_interactions

class TestDatabase_interactions(unittest.TestCase):
    def setUp(self):
        self.db = Database_interactions()

    def test_adding_to_database_unsuccessful(self):
        self.assertEqual(self.db.addinfofromfile("eitoimi.txt"), None)