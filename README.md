# Arkusze.pl Downloader
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/skill3472/ArkuszeDownloader/total?style=flat-square)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/skill3472/ArkuszeDownloader?style=flat-square)

Program stworzony do szybkiego pobierania arkuszy ze strony Arkusze.pl.
Oryginalnie stworzony na własne potrzeby, ale uznałem, że go opublikuje, może komuś się przyda.

## Instalacja
1. Pobierz repozytorium jako .zip
2. Rozpakuj
3. Zainstaluj Pythona i Pipa. [Jak to zrobić?](https://www.youtube.com/watch?v=urmxXHukIGM)
4. Zainstaluj wymagane paczki za pomocą komendy `pip install -r requirements.txt`

## Jak używać?
Zmień potrzebne ustawienia w pliku `config.yaml` i uruchom program za pomocą `python3 app.py`

#

### Kody błędu:
- 201: Numer wybranego arkusza nie jest prawidłowy (musisz podać liczbę).
- 202: Błąd w pobieraniu plików - otwórz Issue na GitHubie i napisz jaki arkusz próbowałeś/aś pobrać
- 203: Nieprawidłowy kod przedmiotu - podaj prawidłowy kod przedmiotu (lista w pliku config.yaml)

### Credits:
- Maksymilian Tym
- Specjalne podziękowania dla autora strony Arkusze.pl (jeśli chcesz, żebym usunął to repozytorium, skontaktuj się ze mną)

### W planach
- Pytanie się użytkownika o przedmiot, zamiast ustawianie go w configu
- Pobieranie słuchania do niektórych arkuszy (np. J. Angielski)
