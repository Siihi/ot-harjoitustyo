from classes import Database_Interactions, User
Db = Database_Interactions()
user = User()


class Service:
    def __init__(self):
        self.UserId = 0

    def index(self):
        print("Tervetuloa budjetointisovellukseen!")
        print("Kirjautuaksesi sisään, paina 1")
        print("Rekisteröityäksesi, paina 2")
        print("Poistaaksesi käyttäjän, paina 3")
        print("Jos haluat poistua, paina 0")
        self.loginchoices()

    def greeting(self):
        print("Hei!")
        print("Jos haluat lisätä tietoja csv-tiedostosta, paina 1")
        print("Jos haluat nähdä kaikki tietosi, paina 2")
        print("Jos haluat nähdä kaikki tulot, paina 3")
        print("Jos haluat nähdä kaikki menot, paina 4")
        print("Jos haluat nähdä kaikki tulot ja menot yhteensä, paina 5")
        print("Jos haluat nähdä kuukauden tulot, paina 6")
        print("Jos haluat nähdä kuukauden menot, paina 7")
        print("Jos haluat nähdä kuukauden tulot ja menot yhteensä, paina 8")
        print("Jos haluat lisätä käteistä, paina 9")
        print("Jos haluat lisätä käteisoston, paina 10")
        print("Jos haluat poistua, paina 0")
        self.choices()

    def loginchoices(self):
        choice = int(input("Valinta:"))
        if choice == 1:
            self.login()
        elif choice == 2:
            self.register()
        elif choice == 3:
            self.deleteuser()
        elif choice == 0:
            pass
        else:
            print("Valitse oikea vaihtoehto")
            self.loginchoices()

    def choices(self):
        while True:
            choice = int(input("Valinta:"))
            if choice == 1:
                self.addinfo()
            elif choice == 2:
                self.fetchallinfos()
            elif choice == 3:
                self.fetchincomeofalltime()
            elif choice == 4:
                self.fetchexpensesofalltime()
            elif choice == 5:
                self.fetchallofalltime()
            elif choice == 6:
                self.fetchincomeofmonth()
            elif choice == 7:
                self.fetchexpensesofmonth()
            elif choice == 8:
                self.fetchallofmonth()
            elif choice == 9:
                self.addcash()
            elif choice == 10:
                self.addcashpurchase()
            elif choice == 0:
                break
            else:
                print("Valitse oikea vaihtoehto")
                continue

    def login(self):
        username = input("Tunnus:")
        password = input("Salasana:")
        login = user.login(username, password)
        if login is False:
            print("Salasana oli väärin tai käyttäjää ei löytynyt")
        else:
            print("Olet nyt kirjautunut")
            self.UserId = login
            self.greeting()

    def register(self):
        username = input("Tunnus:")
        password = input("Salasana:")
        test = input("Salasana uudestaan:")
        if password == test:
            if user.register(username, password):
                print("Olet luonut käyttäjän")
                self.index()
            else:
                print("Ei onnistunut, sillä nimellä on jo käyttäjä")
                self.index()
        else:
            print("Salasanat eivät täsmää")
            self.register()

    def deleteuser(self):
        username = input("Tunnus:")
        password = input("Salasana:")
        confirmation = input("Oletko varma, Kyllä/Ei?")
        if confirmation == "Ei":
            self.index()
        elif confirmation == "Kyllä":
            delete = user.deleteuser(username, password)
            if delete is False:
                print("Käyttäjää ei ole tai salasana on väärä")
            else:
                print("Onnistui!")
                self.index()

    def addinfo(self):
        print("Varmista että tiedosto on data-kansiossa")
        name = input("Anna tiedoston nimi:")
        Db.addinfofromfile(self.UserId, name)

    def addcash(self):
        cash = input("Käteisen määrä (muodossa 0,00):")
        Db.addcash(self.UserId, cash)

    def addcashpurchase(self):
        cash = input("Oston määrä (muodossa -0,00):")
        shop = input("Kauppa:")
        date = input("Päivä (muodossa 30.09.2000):")
        Db.addcashpurchase(self.UserId, cash, shop, date)

    def fetchallinfos(self):
        Db.fetchallinfo(self.UserId)

    def fetchincomeofalltime(self):
        print(Db.fetchincomeofalltime(self.UserId))

    def fetchexpensesofalltime(self):
        print(Db.fetchexpensesofalltime(self.UserId))

    def fetchallofalltime(self):
        income = Db.fetchincomeofalltime(self.UserId)
        expenses = Db.fetchexpensesofalltime(self.UserId)
        print(income+expenses)

    def fetchincomeofmonth(self):
        year = input("Anna vuosi:")
        month = input("Anna kuukausi:")
        print(Db.fetchincomeofmonth(self.UserId, month, year))

    def fetchexpensesofmonth(self):
        year = input("Anna vuosi:")
        month = input("Anna kuukausi:")
        print(Db.fetchexpensesofmonth(self.UserId, month, year))

    def fetchallofmonth(self):
        year = input("Anna vuosi:")
        month = input("Anna kuukausi:")
        income = Db.fetchincomeofmonth(self.UserId, month, year)
        expenses = Db.fetchexpensesofmonth(self.UserId, month, year)
        print(income+expenses)

    #def fetchallfromcategory(self):

    #def addstoretocategory(self):

    #def fetchallfromcategorymonth(self):

    



if __name__ == "__main__":
    X = Service()
    X.index()