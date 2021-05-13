import os
import datetime
from database_connection import get_database_connection
Db = get_database_connection()
Db.isolation_level = None

class User:
    """Käyttäjästä vastaava luokka.
    """
    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kertoo käyttäjän tunnuksen.
            password: Merkkijonoarvo, joka kertoo käyttäjän salasanan.

        Returns:
            Jos kirjautuminen onnistuu, palauttaa käyttäjän id:n.
            Jos käyttäjää ei löydy tai salasana on väärin, palauttaa False.
        """
        search = Db.execute("""
                            SELECT id, username, password
                            FROM Users 
                            WHERE username=?
                            """, [username]).fetchone()
        if search is None:
            return False
        else:
            if search[1] == username and search[2] == password:
                return search[0]
            elif search[1] == username and search[2] != password:
                return False

    def register(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kertoo käyttäjän tunnuksen.
            password: Merkkijonoarvo, joka kertoo käyttäjän salasanan.

        Returns:
            Jos rekisteröityminen onnistuu, palauttaa True.
            Jos samanniminen käyttäjä löytyy jo, palauttaa False.
        """
        overlap = Db.execute("""
                            SELECT 1
                            FROM Users 
                            WHERE username = ?
                            """, [username]).fetchone()
        if overlap is None:
            Db.execute("""
                        INSERT INTO Users (username, password) 
                        VALUES (?,?)
                        """, [username, password])
            return True
        else:
            return False

    def deleteuser(self, username, password):
        """Poistaa olemassaolevan käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kertoo käyttäjän tunnuksen.
            password: Merkkijonoarvo, joka kertoo käyttäjän salasanan.

        Returns:
            Jos poistaminen onnistuu, palauttaa True.
            Jos käyttäjää ei ole tai salasana on väärin, palauttaa False.
        """
        search = Db.execute("""
                            SELECT id, username, password
                            FROM Users 
                            WHERE username=?
                            """, [username]).fetchone()
        if search is None:
            return False
        else:
            if search[1] == username and search[2] == password:
                Db.execute("""
                            DELETE FROM Users
                            WHERE username = ?
                            """, [username])
                return True
            elif search[1] == username and search[2] != password:
                return False

class Database_Interactions:
    """Tilitiedoista vastaava luokka.
    """
    def addinfofromfile(self, user_id, filename):
        """Lisää tietoja csv-tiedostosta tietokantaan.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.
            filename: Merkkijonoarvo, joka kertoo lisättävän tiedoston nimen.

        Returns:
            Jos tiedoston lisääminen onnistuu, palauttaa True.
            Jos tiedostoa ei löydetä, palauttaa False.
        """
        dirname = os.path.dirname(__file__)
        new_path = os.path.join(dirname, "..", "data", filename)
        try:
            open(new_path, "r")
        except FileNotFoundError:
            return False
        with open(new_path, "r") as file1:
            for line in file1:
                edit = line.split(";")
                if edit[0] == "Kirjauspäivä":
                    continue
                for info in edit:
                    info.strip()
                date = edit[0]
                date = datetime.datetime.strptime(date, "%d.%m.%Y")
                date = date.date()
                Db.execute("""
                            INSERT INTO Accounts (User_id, date, amount, account, name, currency) 
                            VALUES (?,?,?,?,?,?)
                            """, [user_id, date, edit[1], edit[2], edit[5], edit[8]])
        return True

    def addcash(self, user_id, cash):
        """Lisää käteistä käyttäjän tilille.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.
            cash: Merkkijonoarvo, joka kertoo lisättävän käteisen määrän.

        Returns:
            Jos käteisen lisääminen onnistuu, palauttaa True.
            Jos käteisen määrä on kirjoitettu väärin, palauttaa False.
        """
        date = datetime.datetime.now()
        date = date.date()
        currency = "EUR"
        if "," not in cash:
            return False
        try:
            trial = cash.replace(",", "")
            int(trial)
        except ValueError:
            return False
        Db.execute("""
                    INSERT INTO Accounts (User_id, date, amount, currency) 
                    VALUES (?,?,?,?)
                    """, [user_id, date, cash, currency])
        return True

    def addcashpurchase(self, user_id, cash, shop, date):
        """Lisää käteisoston käyttäjän tilille.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.
            cash: Merkkijonoarvo, joka kertoo käteisoston määrän.
            shop: Merkkijonoarvo, joka kertoo kaupan nimen jossa osto tehtiin.
            date: Merkkijonoarvo, joka kertoo milloin ostos tehtiin.

        Returns:
            Jos käteisoston lisääminen onnistuu, palauttaa True.
            Jos käteisarvo tai päivämäärä on kirjoitettu väärin, palauttaa False.
        """
        currency = "EUR"
        if "," not in cash or "-" not in cash:
            return False
        try:
            trial = cash.replace(",", "")
            trial = trial.replace("-", "")
            int(trial)
        except ValueError:
            return False
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
        date = date.date()
        Db.execute("""
                    INSERT INTO Accounts (User_id, date, amount, name, currency)
                    VALUES (?,?,?,?,?)
                    """, [user_id, date, cash, shop, currency])
        return True

    def fetchallinfo(self, user_id):
        """Hakee kaikki käyttäjän tilitiedot.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.

        Returns:
            Jos käyttäjällä on tilitietoja, palauttaa nämä listassa.
            Jos tilitietoja ei löydy, palauttaa tyhjän listan.
        """
        infolist = []
        info = Db.execute("""
                            SELECT date, amount, account, name, currency
                            FROM Accounts 
                            WHERE user_id = ? 
                            ORDER BY date ASC
                            """, [user_id]).fetchall()
        for row in info:
            obj = (row[0], row[1], row[2], row[3], row[4])
            infolist.append(obj)
        return infolist

    def fetchincomeofalltime(self, user_id):
        """Hakee käyttäjän kaikki tulot.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.

        Returns:
            Jos käyttäjällä on tuloja, palauttaa niiden summan.
            Jos käyttäjällä ei ole tuloja, palauttaa 0.
        """
        sum_num = 0
        info = Db.execute("""
                            SELECT amount
                            FROM Accounts 
                            WHERE user_id = ?
                            """, [user_id]).fetchall()
        for line in info:
            if line[0][0] == "-":
                continue
            else:
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                sum_num += int(add)
        return sum_num/100

    def fetchexpensesofalltime(self, user_id):
        """Hakee käyttäjän kaikki menot.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.

        Returns:
            Jos käyttäjällä on menoja, palauttaa niiden summan.
            Jos käyttäjällä ei ole menoja, palauttaa 0.
        """
        sum_num = 0
        info = Db.execute("""
                            SELECT amount
                            FROM Accounts 
                            WHERE user_id = ?
                            """, [user_id]).fetchall()
        for line in info:
            if line[0][0] == "-":
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                sum_num += int(add)
            else:
                continue
        return sum_num/100

    def fetchincomeofmonth(self, user_id, month, year):
        """Hakee käyttäjän kuukauden tulot.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.

        Returns:
            Jos käyttäjällä on tuloja, palauttaa niiden summan.
            Jos käyttäjällä ei ole tuloja, palauttaa 0.
        """
        sum_num = 0
        date = year + "-" + month + "%"
        info = Db.execute("""
                            SELECT amount 
                            FROM Accounts 
                            WHERE user_id = ? AND date LIKE ?
                            """, [user_id, date]).fetchall()
        for line in info:
            if line[0][0] == "-":
                continue
            else:
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                sum_num += int(add)
        return sum_num/100

    def fetchexpensesofmonth(self, user_id, month, year):
        """Hakee käyttäjän kuukauden menot.

        Args:
            user_id: Numero, joka kertoo käyttäjän id:n.

        Returns:
            Jos käyttäjällä on menoja, palauttaa niiden summan.
            Jos käyttäjällä ei ole menoja, palauttaa 0.
        """
        sum_num = 0
        date = year + "-" + month + "%"
        info = Db.execute("""
                            SELECT amount 
                            FROM Accounts 
                            WHERE user_id = ? AND date LIKE ?
                            """, [user_id, date]).fetchall()
        for line in info:
            if line[0][0] == "-":
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                sum_num += int(add)
            else:
                continue
        return sum_num/100

user = User()
db = Database_Interactions()
