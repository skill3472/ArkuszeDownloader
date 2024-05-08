# Arkusze.pl Downloader

Program stworzony do szybkiego pobierania arkuszy ze strony Arkusze.pl.
Oryginalnie stworzony na własne potrzeby, ale uznałem, że go opublikuje, może komuś się przyda.

## Instalacja
1. Pobierz repozytorium jako .zip
2. Rozpakuj
3. Zainstaluj Pythona i Pipa. [Jak to zrobić?](https://www.youtube.com/watch?v=urmxXHukIGM)
4. Zainstaluj wymagane paczki za pomocą komendy `pip install -r requirements.txt`

## Jak używać?
Zmień potrzebne ustawienia w pliku `config.yaml` i uruchom program za pomocą `python3 app.py`
## Wersja zaawansowana
```
usage: ArkuszeDownloader [-h] [-s SUBJECT] [-a] [-v]

options:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT, --przedmiot SUBJECT
                        Podaj przedmiot (zastapi przedmiot z config.yaml na to
                        uruchomienie).
  -a, --all, --wszystkie
                        Pobiera wszystkie dostępne arkusze, może zająć trochę
                        czasu.
  -v, --version         Pokaż wersję programu.
```

### Wspierane przedmioty
- J. Angielski
- Informatyka
- Matematyka

### Kody błędu:
- 201: Numer wybranego arkusza nie jest prawidłowy (musisz podać liczbę).
- 202: Błąd w pobieraniu plików - otwórz Issue na GitHubie i napisz jaki arkusz próbowałeś/aś pobrać
- 203: Nieprawidłowy kod przedmiotu - podaj prawidłowy kod przedmiotu (lista w pliku config.yaml)
- 204: Nieprawidlowy numer arkusza, pewnie literowka, jesli nie napisz do mnie.

### Credits:
- Maksymilian Tym
- Specjalne podziękowania dla autora strony Arkusze.pl (jeśli chcesz, żebym usunął to repozytorium, skontaktuj się ze mną)

### W planach
- ~~Pobieranie słuchania do niektórych arkuszy (np. J. Angielski).~~ Na razie feature zamieniony na dodawanie skrótu. PyTube ma błąd i wprowadzenie tego wymaga ode mnie za dużo wysiłku. Jeśli ktoś ma siłę się z tym bawić, zapraszam do otwarcia PR :)
- Dodanie szybszego użycia za pomocą argparse (np. `python3 app.py 2304`) zeby pobrac arkusz z kwietnia 2023
- Dodanie więcej przedmiotów