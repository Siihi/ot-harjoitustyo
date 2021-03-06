# Budjetointisovellus

Sovelluksen avulla käyttäjät voivat tutkia menneitä tilitapahtumiaan ja katsoa kuinka paljon rahaa on mennyt mihinkin tarkoitukseen. Sovellusta voi käyttää useampi käyttäjä, joilla kaikilla näkyy vain omat tilitapahtumansa.

## Uusin release

[Release](https://github.com/Siihi/ot-harjoitustyo/releases/tag/v1.0.0)

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.6.0`.

## Dokumentaatio

* [Arkkitehtuurikuvaus](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
* [Testausdokumentti](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
* [Tuntikirjanpito](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
* [Vaatimusmäärittely](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen


Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](https://github.com/Siihi/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
