# Budjetointisovellus

Sovelluksen avulla käyttäjät voivat tutkia menneitä tilitapahtumiaan ja katsoa >
Sovellusta voi käyttää useampi käyttäjä, joilla kaikilla näkyy vain omat tilita>

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.6.0`.

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/Siihi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Tuntikirjanpito](https://github.com/Siihi/ot-harjoitustyo/blob/master/tuntikirjanpito.md)

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
poetry invoke start
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
