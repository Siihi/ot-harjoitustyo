import os
from database_connection import get_database_connection
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
                Db.execute("""
                            INSERT INTO Accounts (UserId, date, amount, account, name, currency) 
                            VALUES (?,?,?,?,?,?)
                            """, [UserId, edit[0], edit[1], edit[2], edit[5], edit[8]])
        print("Onnistui!")

    def fetchallinfo(self, UserId):
        info = Db.execute("""
                            SELECT date, amount, account, name, currency
                            FROM Accounts 
                            WHERE user_id = ?
                            """, [UserId]).fetchall()
        for line in info:
            print(f"{line[0]} | {line[1]} | {line[2]} | {line[3]} | {line[4]}")

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
        print(Sum/100)

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
        print(Sum/100)

    def fetchincomeofmonth(self, UserId, month, year):
        Sum = 0
        date = "%" + str(month) + "." + year
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
        print(Sum/100)

    def fetchexpensesofmonth(self, UserId, month, year):
        Sum = 0
        date = "%" + str(month) + "." + year
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
        print(Sum/100)