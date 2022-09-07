import requests
from bs4 import BeautifulSoup
import re


def get_timetable(phpsessid):
    if not phpsessid:
        return "You need set phpsessid!"
    cookies = {
        'PHPSESSID': phpsessid,
    }

    headers = {
        'Referer': 'https://accounts.google.com.ua/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    response = requests.get('https://timetable.gbmc.ac.uk/', cookies=cookies, headers=headers)

    data = BeautifulSoup(response.text, "html.parser")

    days = []

    for obj in data.findAll("div", {"class": "day"}):
        days.append(obj.get_text().strip())

    subjects = []

    for obj in data.findAll("div", {"class": "col-6"}):
        subject_info = obj.get_text()
        subject_info = re.sub(' +', ' ',subject_info)
        subject_info = re.sub(r'\t+', ' ',subject_info)
        subject_info= subject_info.strip()
        subjects.append(subject_info.splitlines(False))

    timetable = []

    for i in range(len(days)):
        timetable.append({
            "day": days[i],
            "subject": f"{subjects[i][0][9:-1]}",
            "lecturer": f"{subjects[i][1][11:-1]}",
            "room": f"{subjects[i][2][7:-1] if 'Room: ' in subjects[i][2] else subjects[i][2][1:-1]}",
            "startTime": f"{subjects[i][3][13:]}",
            "endTime": f"{subjects[i][4][11:]}"
        })
    
    return timetable