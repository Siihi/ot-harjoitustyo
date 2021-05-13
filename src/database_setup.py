from database_connection import get_database_connection

class DataBase:
    """Tietokannasta vastaava luokka."""
    def create_tables(self, connection):
        """Luo tietokantaan taulut.

        Args:
            connection: Merkkijonoarvo, joka kertoo tietokannan sijainnin.

        Returns:
            Kun tietokannan taulut on alustettu, palauttaa True
        """
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE Users 
                        (id INTEGER PRIMARY KEY, 
                        username TEXT, 
                        password TEXT
                        );""")

        cursor.execute("""CREATE TABLE Accounts
                        (id INTEGER PRIMARY KEY, 
                        user_id INTEGER REFERENCES Users, 
                        date DATE, 
                        amount INT, 
                        account TEXT, 
                        name TEXT, 
                        currency TEXT
                        );""")
        return True

    def drop_tables(self, connection):
        """Poistaa tietokannasta taulut.

        Args:
            connection: Merkkijonoarvo, joka kertoo tietokannan sijainnin.

        Returns:
            Kun tietokannan taulut on tuhottu, palauttaa True.
        """
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Users;")
        cursor.execute("DROP TABLE IF EXISTS Accounts;")
        return True
    
    def insert_test_user(self, connection):
        """Luo tietokantaan testikäyttäjän.

        Args:
            connection: Merkkijonoarvo, joka kertoo tietokannan sijainnin.

        Returns:
            Kun tietokantaan on luotu testikäyttäjä, palauttaa True.
        """
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Users
                        (id, username, password)
                        VALUES (?,?,?)""", 
                        [1,"testi", "testi"])
        return True
        
    def initialize_database(self):
        """Tuhoaa nykyiset taulut tietokannasta, 
        jonka jälkeen luo ne uudelleen ja lisää testikäyttäjän.
        """
        connection = get_database_connection()
        connection.isolation_level = None

        self.drop_tables(connection)
        self.create_tables(connection)
        self.insert_test_user(connection)

db = DataBase()
db.initialize_database()
