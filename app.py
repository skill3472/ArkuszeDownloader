#!/usr/bin/python
import os.path
import yaml as yml
import arkusze_utils as ark
import argparse

CONFIG_FILE = 'config.yaml'

with open(CONFIG_FILE, 'r') as stream:
    CONFIG = yml.safe_load(stream)

URL = CONFIG['url']

parser = argparse.ArgumentParser(prog='ArkuszeDownloader')
parser.add_argument('arkusz', nargs='?', help='Podaj numer arkusza (format YYMM, czyli np. 2305) do pobrania.')
parser.add_argument('-s', '--subject', '--przedmiot', required=False,
                    help="Podaj przedmiot (zastapi przedmiot z config.yaml na to uruchomienie).")
parser.add_argument('-o', '--output', required=False, help='Podaj scieżkę zapisania arkusza/y (zastapi ścieżkę z config.yaml na to uruchomienie). Musi się kończyć na /')
parser.add_argument('-l', '--list', required=False, action='store_true', help='Pokazuje dostępne kody przedmiotów.')
parser.add_argument('-a', '--all', '--wszystkie', action='store_true',
                    help="Pobiera wszystkie dostępne arkusze, może zająć trochę czasu.")
parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.2', help="Pokaż wersję programu.")
args = parser.parse_args()

if args.list:
    [print(entry) for entry in CONFIG['available_subjects']]
    quit(0)

if args.arkusz and not ark.IsValidDateCode(args.arkusz):
    print("Podano nieprawidłowy format kodu (wymagany format MMYY).")
    quit(205)

used_subject = CONFIG['used_subject']
if args.subject:
    used_subject = args.subject
if used_subject not in CONFIG['available_subjects']:
    quit(203)
subject_url = URL + ark.GetPathFromCode(used_subject)

arkusze = ark.GetSheetsDictFromUrl(subject_url)
wybrane_arkusze = None
if args.arkusz:
    if ark.GetSheetFromDateCode(args.arkusz, arkusze):
        wybrane_arkusze = [ark.GetSheetFromDateCode(args.arkusz, arkusze)]
elif not args.all:
    i = 0
    for arkusz in arkusze:
        i += 1
        print(f'{i}. {arkusz["date"]} - {arkusz["name"]}')

    selected = int(input('Wybierz arkusz do pobrania: '))

if not args.all and not args.arkusz:
    try:
        i = 0
        for arkusz in arkusze:
            i += 1
            if i == selected:
                wybrane_arkusze = [arkusz]
                break
    except ValueError:
        print("Podano nieprawidlowy numer arkusza.")
        quit(204)
elif not args.arkusz:
    wybrane_arkusze = arkusze

if wybrane_arkusze is None:
    print('To nie jest prawidlowy arkusz!')
    quit(201)

download_to = CONFIG['download_to']
if args.output and os.path.exists(args.output):
    download_to = args.output


for arkusz in wybrane_arkusze:
    print("Pobieram arkusz...")

    wybrany_url = arkusz['href']
    zalaczniki = ark.GetAttachmentUrlsFromUrl(wybrany_url)
    path = download_to + used_subject
    ark.CreateDirSafe(path)
    if CONFIG['month_codes']:
        path += "/" + ark.DateToDatecode(arkusz['date'])
    else:
        path += "/" + arkusz['date']
    ark.CreateDirSafe(path)
    for zalacznik in zalaczniki:
        ark.DownloadFileFromUrl(zalacznik, path)
    print("Pobrano arkusze!")
    ytID = ark.GetYoutubeIDFromUrl(wybrany_url)
    if ytID and CONFIG["add_shortcut"]:
        print("Dodaje skrót do YouTube...")
        if ark.CreateYoutubeShortcut(ytID, path):
            print("Pomyślnie dodano skrót!")
