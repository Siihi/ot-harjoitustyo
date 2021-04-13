from database_connection import get_database_connection
import os


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Database_interactions:
    def addinfofromfile(self, filename):
        user_id = 0 #Tähän user id kirjautumisen jälkeen
        new_path = os.path.relpath("../csv/"+filename)
        try:
            open(new_path, "r")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt")
            return
        with open(new_path, "r") as file1:
            db = get_database_connection()
            db.isolation_level = None
            for line in file1:
                edit = line.split(";")
                if edit[0] == "Kirjauspäivä":
                    continue
                for info in edit:
                    info.strip()
                db.execute("INSERT INTO Accounts (user_id, date, amount, account, name, currency) VALUES (?,?,?,?,?,?)",[user_id, edit[0], edit[1], edit[2], edit[5], edit[8]])
        print("Onnistui!")