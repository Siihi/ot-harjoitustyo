from database_connection import get_database_connection

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Users (id TEXT PRIMARY KEY, username TEXT, password TEXT);")
    cursor.execute("CREATE TABLE Accounts (id TEXT PRIMARY KEY, user_id INTEGER REFERENCES Users, date DATE, amount INT, account TEXT, name TEXT, currency TEXT);")

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Users;")
    cursor.execute("DROP TABLE IF EXISTS Accounts;")
    
def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
