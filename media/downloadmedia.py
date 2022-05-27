from iovoice.output import speak
from iovoice.input import voiceinput
import requests as req
import pafy as ytd
import re
import os

SEARCH_URL = "https://www.youtube.com/results?search_query={}"
WATCH_URL = "https://www.youtube.com/{}"
REGEX_WATCH = "watch\?v=[a-zA-Z0-9\-_]+"
DOWNLOAD_PATH = os.path.join(
    os.getcwd(),
    "downloads"
)

# from bs4 import BeautifulSoup

# create the folder to contain the online downloaded media
try:
    os.mkdir("downloads")
except:pass

def searchonline(term,/):
    response = req.get(SEARCH_URL.format(term.replace(" ","+"))).text
    watch_ids = re.findall(REGEX_WATCH,response)
    # print(watch_ids)
    # extract the information from each watch id
    for x,wid in enumerate(watch_ids):
        temp = ytd.new(WATCH_URL.format(wid))
        print(f"{x} -> {temp.title}") 
    speak("Pick any one song or you pick multiple seperated using commas")
    picks = input().split(",")
    if picks[0].lower() == "all":
        for x in watch_ids:
            save(x)
    else:
        for x in picks:
            if int(x) < 0 or int(x) > len(watch_ids):
                break
        else:
            if len(picks) > 1:
                for x in picks:
                    save(watch_ids[int(x)])
            elif len(picks) == 1:
                save(watch_ids[int(picks[0])])
            else:
                speak("Invalid Input")

def save(watch_id,/):
    media = ytd.new(WATCH_URL.format(watch_id))
    ch = voiceinput("What do you wanna download? video or audio")
    if ch in 'audio':
        temp = media.getbestaudio()
        temp.download(filepath = DOWNLOAD_PATH,quiet=True)
    else:
        temp = media.getbest()
        temp.download(filepath = DOWNLOAD_PATH,quiet=True)


