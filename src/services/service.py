import datetime
from classes import user, db

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class Service:
    """Käyttäjästä ja budjetoinnista vastaava luokka."""
    def __init__(self):
        """Luokan konstruktori. Luo pohjan käyttäjän id:lle."""
        self.user = None

    def current_user(self):
        """Palauttaa tämän hetkisen käyttäjän id:n.

        Returns:
            Käyttäjän id.
        """
        return self.user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, kirjautuvan käyttäjän käyttäjätunnus.
            password: Merkkijonoarvo, kirjautuvan käyttäjän salasana.

        Raises:
            InvalidCredentialsError: 
                Virhe, joka tapahtuu kun käyttäjätunnus tai salasana on väärin.
        """
        login = user.login(username, password)
        if login is False:
            raise InvalidCredentialsError("Väärä käyttäjänimi tai salasana")
        self.user = login

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self.user = None

    def register(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, luotava käyttäjätunnus.
            password: Merkkijonoarvo, luotava salasana.

        Raises:
            UsernameExistsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus on jo olemassa.
        """
        register = user.register(username, password)
        if register is False:
            raise UsernameExistsError("Käyttäjä on jo olemassa")

    def deleteuser(self, username, password):
        """Poistaa olemassa olevan käyttäjän.

        Args:
            username: Merkkijonoarvo, poistettava käyttäjätunnus.
            password: Merkkijonoarvo, poistettava salasana.

        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjää ei löydy tietokannasta. 
        """
        delete = user.deleteuser(username, password)
        if delete is False:
            raise InvalidCredentialsError("Käyttäjää ei löydy")

    def addinfo(self, name):
        """Lisää tietoja csv-tiedostosta.

        Args:
            name: Merkkijonoarvo, lisättävän tiedoston nimi.

        Raises:
            InvalidCredentialsError: 
                Virhe, joka tapahtuu, kun tiedostoa ei löydy.
        """
        addinfo = db.addinfofromfile(self.user, name)
        if addinfo is False:
            raise InvalidCredentialsError("Tiedostoa ei löytynyt")

    def addcash(self, cash):
        """Lisää käteistä käyttäjälle.

        Args:
            cash: Merkkijonoarvo, käteisen määrä.

        Raises:
            InvalidCredentialsError: 
                Virhe, joka tapahtuu, kun rahamäärä on kirjoitettu väärin. 
        """
        addcash = db.addcash(self.user, cash)
        if addcash is False:
            raise InvalidCredentialsError("Rahamäärä kirjoitettu väärin")

    def addcashpurchase(self, cash, shop, date):
        """Lisää käteisosto käyttäjälle.

        Args:
            cash: Merkkijonoarvo, oston määrä.
            shop: Merkkijonoarvo, kaupan nimi.
            date: Merkkijonoarvo, päivä milloin ostos tehtiin.

        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun rahamäärä tai päivämäärä on kirjoitettu väärin.
        """
        addcashpurchase = db.addcashpurchase(self.user, cash, shop, date)
        if addcashpurchase is False:
            raise InvalidCredentialsError("Rahamäärä tai päivämäärä kirjoitettu väärin")

    def fetchallinfos(self):
        """Hakee kaikki käyttäjän tiedot.

        Returns:
            Palauttaa kirjautuneen käyttäjän kaikki tilitiedot listana.
            Jos tilitietoja ei ole, palauttaa tyhjän listan.
        """
        return db.fetchallinfo(self.user)

    def fetchincomeofalltime(self):
        """Hakee käyttäjän kaikki tulot.

        Returns:
            Palauttaa käyttäjän kaikki tulot summattuna yhteen.
        """
        return db.fetchincomeofalltime(self.user)

    def fetchexpensesofalltime(self):
        """Hakee käyttäjän kaikki menot.

        Returns:
            Palauttaa käyttäjän kaikki menot summattuna yhteen.
        """
        return db.fetchexpensesofalltime(self.user)

    def fetchincomeofmonth(self):
        """Hakee käyttäjän kaikki tulot tämänhetkiseltä kuukaudelta.

        Returns:
            Palauttaa käyttäjän kuukauden tulot summattuna yhteen.
        """
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        if len(month) == 1:
            month = "0" + month
        return db.fetchincomeofmonth(self.user, month, year)

    def fetchexpensesofmonth(self):
        """Hakee käyttäjän kaikki menot tämänhetkiseltä kuukaudelta.

        Returns:
            Palauttaa käyttäjän kuukauden menot summattuna yhteen.
        """
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        if len(month) == 1:
            month = "0" + month
        return db.fetchexpensesofmonth(self.user, month, year)

service = Service()
