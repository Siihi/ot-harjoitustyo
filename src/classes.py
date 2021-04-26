import os
from database_connection import get_database_connection
import datetime
Db = get_database_connection()
Db.isolation_level = None

class User:
    def login(self, username, password):
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
    def addinfofromfile(self, UserId, filename):
        dirname = os.path.dirname(__file__)
        new_path = os.path.join(dirname, "..", "data", filename)
        try:
            open(new_path, "r")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt")
            return
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
                            """, [UserId, date, edit[1], edit[2], edit[5], edit[8]])
        print("Onnistui!")
        return True

    def addcash(self, UserId, cash):
        date = datetime.datetime.now()
        date = date.date()
        currency = "EUR"
        if "," not in cash:
            print("Rahamäärä kirjoitettu väärin")
            return
        Db.execute("""
                    INSERT INTO Accounts (User_id, date, amount, currency) 
                    VALUES (?,?,?,?)
                    """, [UserId, date, cash, currency])
        print("Onnistui!")
        return True

    def addcashpurchase(self, UserId, cash, shop, date):
        currency = "EUR"
        if "," not in cash or "-" not in cash:
            print("Rahamäärä kirjoitettu väärin")
            return
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
        date = date.date()
        Db.execute("""
                    INSERT INTO Accounts (User_id, date, amount, name, currency)
                    VALUES (?,?,?,?,?)
                    """, [UserId, date, cash, shop, currency])
        print("Onnistui!")
        return True

    def fetchallinfo(self, UserId):
        info = Db.execute("""
                            SELECT date, amount, account, name, currency
                            FROM Accounts 
                            WHERE user_id = ? 
                            ORDER BY date ASC
                            """, [UserId]).fetchall()
        for line in info:
            print(f"{line[0]} | {line[1]} | {line[2]} | {line[3]} | {line[4]}")
        return True

    def fetchincomeofalltime(self, UserId):
        Sum = 0
        info = Db.execute("""
                            SELECT amount
                            FROM Accounts 
                            WHERE user_id = ?
                            """, [UserId]).fetchall()
        for line in info:
            if line[0][0] == "-":
                continue
            else:
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                Sum += int(add)
        return Sum/100

    def fetchexpensesofalltime(self, UserId):
        Sum = 0
        info = Db.execute("""
                            SELECT amount
                            FROM Accounts 
                            WHERE user_id = ?
                            """, [UserId]).fetchall()
        for line in info:
            if line[0][0] == "-":
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                Sum += int(add)
            else:
                continue
        return Sum/100

    def fetchincomeofmonth(self, UserId, month, year):
        Sum = 0
        if len(month) == 1:
            month = "0" + month
        date = year + "-" + month + "%"
        info = Db.execute("""
                            SELECT amount 
                            FROM Accounts 
                            WHERE user_id = ? AND date LIKE ?
                            """, [UserId, date]).fetchall()
        for line in info:
            if line[0][0] == "-":
                continue
            else:
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                Sum += int(add)
        return Sum/100

    def fetchexpensesofmonth(self, UserId, month, year):
        Sum = 0
        if len(month) == 1:
            month = "0" + month
        date = year + "-" + month + "%"
        info = Db.execute("""
                            SELECT amount 
                            FROM Accounts 
                            WHERE user_id = ? AND date LIKE ?
                            """, [UserId, date]).fetchall()
        for line in info:
            if line[0][0] == "-":
                add = line[0]
                if "," in add:
                    add = add.replace(",", "")
                Sum += int(add)
            else:
                continue
        return Sum/100