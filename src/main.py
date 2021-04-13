from classes import Database_interactions

def greeting():
    print("Hei!")
    print("Jos haluat poistua, paina 0")
    print("Jos haluat lisätä tietoja csv-tiedostosta, paina 1")

while True:
    greeting()
    choice = int(input("Valinta:"))
    if choice == 1:
        print("Varmista että tiedosto on csv-kansiossa")
        name = input("Anna tiedoston nimi:")
        db = Database_interactions()
        db.addinfofromfile(name)
    if choice == 0:
        break