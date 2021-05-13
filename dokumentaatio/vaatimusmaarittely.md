# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat tutkia menneitä tilitapahtumiaan ja katsoa kuinka paljon rahaa on mennyt mihinkin tarkoitukseen.
Sovellusta voi käyttää useampi käyttäjä, joilla kaikilla näkyy vain omat tilitapahtumansa.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli eli normaali käyttäjä.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjä voi luoda käyttäjätunnuksen
    - Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään olemassaolevalla käyttäjätunnuksella ja salasanalla
    - Ohjelma ilmoittaa jos tunnusta ei ole olemassa tai salasana on väärä
- Käyttäjä voi poistaa tunnuksen
    - Poistaminen tapahtuu kun käyttäjä syöttää olemassaolevan tunnuksen ja salasanan
    - Ohjelma ilmoittaa jos tunnusta ei ole olemassa tai salasana on väärä

### Kirjautumisen jälkeen

- Käyttäjä voi syöttää järjestelmään omat tilitapahtumansa csv-tiedoston avulla
- Käyttäjä näkee kaikki syötetyt tilitiedot listassa
- Käyttäjä näkee viime kaikki/kuukauden tulot ja menot
- Käyttäjä näkee paljonko rahaa hänelle on jäänyt yli kuukaudessa
- Käyttäjä voi lisätä käteistä ja ostoja tilitapahtumiin
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

- Säästöjen, eli paljonko rahaa pitäisi ainakin olla tilillä, näyttäminen ja muokkaaminen
- Kategorioiden luominen ja tapahtumien lajitteleminen
- Tapahtumien piilotus tilastoista
- Suunnitelmien luominen seuraavalle kuukaudelle aikaisempien tilastojen perusteella
- Käyttäjätiimit, jotka näkevät yhteiset budjetit
