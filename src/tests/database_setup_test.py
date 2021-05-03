import unittest
from database_setup import DataBase
from database_connection import get_database_connection

class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase()
        self.connection = get_database_connection()
        self.connection.isolation_level = None

    def test_create_tables_successful(self):
        self.db.drop_tables(self.connection)
        self.assertEqual(self.db.create_tables(self.connection), True)
        self.db.initialize_database()

    def test_drop_tables_successful(self):
        self.assertEqual(self.db.drop_tables(self.connection), True)
        self.db.initialize_database()

    def test_insert_test_user(self):
        self.db.drop_tables(self.connection)
        self.db.create_tables(self.connection)
        self.assertEqual(self.db.insert_test_user(self.connection), True)
        self.db.drop_tables(self.connection)
        self.db.initialize_database()