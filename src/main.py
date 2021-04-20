from classes import Database_Interactions, User
Db = Database_Interactions()
user = User()
UserId = 0

def index():
    print("Tervetuloa budjetointisovellukseen!")
    print("Kirjautuaksesi sisään, paina 1")
    print("Rekisteröityäksesi, paina 2")
    print("Poistaaksesi käyttäjän, paina 3")
    print("Jos haluat poistua, paina 0")
    loginchoices()

def greeting():
    print("Hei!")
    print("Jos haluat lisätä tietoja csv-tiedostosta, paina 1")
    print("Jos haluat nähdä kaikki tietosi, paina 2")
    print("Jos haluat nähdä kaikki tulot, paina 3")
    print("Jos haluat nähdä kaikki menot, paina 4")
    print("Jos haluat nähdä kuukauden tulot, paina 5")
    print("Jos haluat nähdä kuukauden menot, paina 6")
    print("Jos haluat poistua, paina 0")
    choices()


def loginchoices():
    choice = int(input("Valinta:"))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 3:
        deleteuser()
    elif choice == 0:
        pass
    else:
        print("Valitse oikea vaihtoehto")
        loginchoices()

def choices():
    while True:
        choice = int(input("Valinta:"))
        if choice == 1:
            addinfo()
        elif choice == 2:
            fetchallinfos()
        elif choice == 3:
            fetchincomeofalltime()
        elif choice == 4:
            fetchexpensesofalltime()
        elif choice == 5:
            fetchincomeofmonth()
        elif choice == 6:
            fetchexpensesofmonth()
        elif choice == 0:
            break
        else:
            print("Valitse oikea vaihtoehto")
            continue

def login():
    username = input("Tunnus:")
    password = input("Salasana:")
    login = user.login(username, password)
    if login is False:
        print("Salasana oli väärin tai käyttäjää ei löytynyt")
    else:
        print("Olet nyt kirjautunut")
        global UserId
        UserId = login
        greeting()

def register():
    username = input("Tunnus:")
    password = input("Salasana:")
    test = input("Salasana uudestaan:")
    if password == test:
        if user.register(username, password):
            print("Olet luonut käyttäjän")
            index()
        else:
            print("Ei onnistunut, sillä nimellä on jo käyttäjä")
            index()
    else:
        print("Salasanat eivät täsmää")
        register()

def deleteuser():
    username = input("Tunnus:")
    password = input("Salasana:")
    confirmation = input("Oletko varma, Kyllä/Ei?")
    if confirmation == "Ei":
        index()
    elif confirmation == "Kyllä":
        delete = user.deleteuser(username, password)
        if delete is False:
            print("Käyttäjää ei ole tai salasana on väärä")
        else:
            print("Onnistui!")
            index()

def addinfo():
    print("Varmista että tiedosto on data-kansiossa")
    name = input("Anna tiedoston nimi:")
    Db.addinfofromfile(UserId, name)

def fetchallinfos():
    Db.fetchallinfo(UserId)

def fetchincomeofalltime():
    Db.fetchincomeofalltime(UserId)

def fetchexpensesofalltime():
    Db.fetchexpensesofalltime(UserId)

def fetchincomeofmonth():
    year = input("Anna vuosi:")
    month = input("Anna kuukausi:")
    Db.fetchincomeofmonth(UserId, month, year)

def fetchexpensesofmonth():
    year = input("Anna vuosi:")
    month = input("Anna kuukausi:")
    Db.fetchexpensesofmonth(UserId, month, year)

if __name__ == "__main__":
    index()