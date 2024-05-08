﻿import os
import requests as req
from bs4 import BeautifulSoup
import re

CODE_TO_PATH = {
    "ANG8SP": "jezyk-angielski-egzamin-osmoklasisty/",
    "ANGP": "jezyk-angielski-matura-poziom-podstawowy/",
    "ANGR": "jezyk-angielski-matura-poziom-rozszerzony/",
    "INFR": "informatyka-matura-poziom-rozszerzony/",
    "MAT8SP": "matematyka-egzamin-osmoklasisty/",
    "MATP": "matematyka-matura-poziom-podstawowy/",
    "MATR": "matematyka-matura-poziom-rozszerzony/"
}
MONTH_TO_NUMBER = {
    "Styczeń": "01",
    "Luty": "02",
    "Marzec": "03",
    "Kwiecień": "04",
    "Maj": "05",
    "Czerwiec": "06",
    "Lipiec": "07",
    "Sierpień": "08",
    "Wrzesień": "09",
    "Październik": "10",
    "Listopad": "11",
    "Grudzień": "12"
}



def GetPathFromCode(code) -> str:
    return CODE_TO_PATH[code]


def GetSheetsDictFromUrl(subject_url):
    subject_page = req.get(subject_url)
    subject_soup = BeautifulSoup(subject_page.content, 'html.parser')
    tabela_arkuszy = subject_soup.findAll('tbody', class_='row-hover')
    tabela_arkuszy = tabela_arkuszy[0]

    arkusze = []
    for arkusz in tabela_arkuszy.findAll('tr'):
        try:
            obj = {}
            date = arkusz.find('td', class_='column-1').string
            obj['date'] = date
            href = arkusz.find('a')['href']
            obj['href'] = href
            name = arkusz.find('a').string
            obj['name'] = name

            arkusze.append(obj)
        except TypeError:
            continue

    return arkusze


def GetAttachmentUrlsFromUrl(sheet_url):
    sheet_page = req.get(sheet_url)
    sheet_soup = BeautifulSoup(sheet_page.content, 'html.parser')
    attachments = []
    for attachment in sheet_soup.findAll('div', class_='msgbox msgbox-arkusz'):
        attachments.append(attachment.find('a')['href'])

    return attachments


def DownloadFileFromUrl(file_url, target_path="."):
    r = req.get(file_url)
    match = re.search(r"[^\/]+(?=(\.pdf|\.zip)$)", file_url)
    if not match:
        return False
    filename = match.group(0) + match.group(1)
    print(filename)
    if r.status_code == 200:
        with open(f'{target_path}/{filename}', 'wb') as f:
            f.write(r.content)
            f.close()
            return True
    else:
        return False


def CreateDirSafe(dirName) -> bool:
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        return True
    else:
        return False


def DateToDatecode(date):
    year = date.split(' ')[1]
    month = date.split(' ')[0]
    yearCode = year[2:]
    monthCode = MONTH_TO_NUMBER[month]
    return yearCode + monthCode


def GetYoutubeIDFromUrl(url) -> str or None:
    r = req.get(url)
    html = r.text
    exp = r"&quot;youtubeID&quot;:&quot;(.{11})&quot;"
    match = re.search(exp, html)
    if match and match.group(1):
        return match.group(1)
    else:
        return None


def CreateYoutubeShortcut(video_id, target_path=".") -> bool:
    url = 'https://www.youtube.com/watch?v=' + video_id
    path = target_path + "/Nagranie.url"
    try:
        with open(path, 'w') as f:
            f.write('[InternetShortcut]\n')
            f.write(f'URL={url}')
            f.close()
            return True
    except:
        return False