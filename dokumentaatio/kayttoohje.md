# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi *Assets*-osion alta *Source code*.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```
## Kirjautuminen

Sovellus käynnistuu kirjautumisnäkymään. Kirjautuminen onnistuu syöttämällä olemassaoleva käyttäjätunnus ja salasana ja painamalla *Kirjaudu sisään*-painiketta.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään painamalla *Rekisteröidy*-nappia.
Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla *Luo*-nappia.

Jos käyttäjän luominen onnistuu, siirrytään päänäkymään.

## Käyttäjän poistaminen

Kirjautumisnäkymästä on mahdollista siirtyä käyttäjän poistonäkymään painamalla *Poista käyttäjä*-nappia.
Käyttäjä poistetaan syöttämällä tiedot syötekenttiin ja painamalla *OK*-nappia.

Jos käyttäjän poistaminen onnistuu, siirrytään kirjautumisnäkymään.

## Päänäkymä

Onnistuneen kirjautumisen myötä siirrytään päänäkymään, josta löytyy tietoja tilitapahtumista.
Näkymästä voi siirtyä lisäämään tietoja csv-tiedostosta, käteisenä tai käteisostoina.
Klikkaamalla painiketta *Kirjaudu ulos* käyttäjä kirjautuu ulos ja sovellus palaa kirjautumisnäkymään.

## Tietoja csv-tiedostosta

Päänäkymästä on mahdollista siirtyä tietojen lisäysnäkymään painamalla *Lisää tietoja*-nappia.
Tietoja lisätään syöttämällä tiedoston nimi kenttään ja painamalla *OK*-nappia.

Jos tietojen lisääminen onnistuu, siirrytään takaisin päänäkymään.

## Käteisen lisääminen

Päänäkymästä on mahdollista siirtyä käteisen lisäysnäkymään painamalla *Lisää käteistä*-nappia.
Tietoja lisätään syöttämällä käteisen määrä kenttään ja painamalla *OK*-nappia.

Jos käteisen lisääminen onnistuu, siirrytään takaisin päänäkymään.

## Käteisoston lisääminen

Päänäkymästä on mahdollista siirtyä käteisoston lisäysnäkymään painamalla *Lisää käteisosto*-nappia.
Tietoja lisätään syöttämällä käteisoston määrä, kaupan nimi ja päivämäärä kenttiin ja painamalla *OK*-nappia.

Jos käteisoston lisääminen onnistuu, siirrytään takaisin päänäkymään.
