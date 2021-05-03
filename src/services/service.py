import datetime
from classes import user, db

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class Service:
    def __init__(self):
        self.user = None

    def current_user(self):
        return self.user

    def login(self, username, password):
        login = user.login(username, password)
        if login is False:
            raise InvalidCredentialsError("Väärä käyttäjänimi tai salasana")
        self.user = login

    def logout(self):
        self.user = None

    def register(self, username, password):
        register = user.register(username, password)
        if register is False:
            raise UsernameExistsError("Käyttäjä on jo olemassa")

    def deleteuser(self, username, password):
        delete = user.deleteuser(username, password)
        if delete is False:
            raise InvalidCredentialsError("Käyttäjää ei löydy")

    def addinfo(self, name):
        addinfo = db.addinfofromfile(self.user, name)
        if addinfo is False:
            raise InvalidCredentialsError("Tiedostoa ei löytynyt")

    def addcash(self, cash):
        addcash = db.addcash(self.user, cash)
        if addcash is False:
            raise InvalidCredentialsError("Rahamäärä kirjoitettu väärin")

    def addcashpurchase(self, cash, shop, date):
        addcashpurchase = db.addcashpurchase(self.user, cash, shop, date)
        if addcashpurchase is False:
            raise InvalidCredentialsError("Rahamäärä tai päivämäärä kirjoitettu väärin")

    def fetchallinfos(self):
        return db.fetchallinfo(self.user)

    def fetchincomeofalltime(self):
        return db.fetchincomeofalltime(self.user)

    def fetchexpensesofalltime(self):
        return db.fetchexpensesofalltime(self.user)

    def fetchincomeofmonth(self):
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        if len(month) == 1:
            month = "0" + month
        return db.fetchincomeofmonth(self.user, month, year)

    def fetchexpensesofmonth(self):
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        if len(month) == 1:
            month = "0" + month
        return db.fetchexpensesofmonth(self.user, month, year)

service = Service()
