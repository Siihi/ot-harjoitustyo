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
        print("Jos haluat nähdä kuukauden tulot, paina 5")
        print("Jos haluat nähdä kuukauden menot, paina 6")
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
                self.fetchincomeofmonth()
            elif choice == 6:
                self.fetchexpensesofmonth()
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

    def fetchallinfos(self):
        Db.fetchallinfo(self.UserId)

    def fetchincomeofalltime(self):
        Db.fetchincomeofalltime(self.UserId)

    def fetchexpensesofalltime(self):
        Db.fetchexpensesofalltime(self.UserId)

    def fetchincomeofmonth(self):
        year = input("Anna vuosi:")
        month = input("Anna kuukausi:")
        Db.fetchincomeofmonth(self.UserId, month, year)

    def fetchexpensesofmonth(self):
        year = input("Anna vuosi:")
        month = input("Anna kuukausi:")
        Db.fetchexpensesofmonth(self.UserId, month, year)

if __name__ == "__main__":
    X = Service()
    X.index()