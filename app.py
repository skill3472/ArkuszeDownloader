import yaml as yml
import arkusze_utils as ark

CONFIG_FILE = 'config.yaml'

with open(CONFIG_FILE, 'r') as stream:
    CONFIG = yml.safe_load(stream)

URL = CONFIG['url']
if CONFIG['used_subject'] not in CONFIG['available_subjects']:
    quit(203)
subject_url = URL + ark.GetPathFromCode(CONFIG['used_subject'])

arkusze = ark.GetSheetsDictFromUrl(subject_url)

i = 0
for arkusz in arkusze:
    i += 1
    print(f'{i}. {arkusz['date']} - {arkusz["name"]}')

selected = int(input('Wybierz arkusz do pobrania: '))
wybrany_arkusz = None
i = 0
for arkusz in arkusze:
    i += 1
    if i == selected:
        wybrany_arkusz = arkusz
        break

if wybrany_arkusz is None:
    print('To nie jest prawidlowy arkusz!')
    quit(201)

wybrany_url = wybrany_arkusz['href']
zalaczniki = ark.GetAttachmentUrlsFromUrl(wybrany_url)
path = CONFIG['download_to'] + CONFIG['used_subject']
ark.CreateDirSafe(path)
if CONFIG['month_codes']:
    path += "/" + ark.DateToDatecode(wybrany_arkusz['date'])
else:
    path += "/" + wybrany_arkusz['date']
ark.CreateDirSafe(path)
for zalacznik in zalaczniki:
    if not ark.DownloadFileFromUrl(zalacznik, path):
        print("Blad w pobieraniu plikow!")
        quit(202)
print("Pobrano pliki!")