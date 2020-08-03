"""
    upload_file_directly.py

    MediaWiki API Demos
    Demo of `Upload` module: Sending post request to upload a file directly

    MIT license
"""

import requests
from secrets import WIKI_BOT_USER, WIKI_BOT_PASS

S = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"
# FILE_PATH = "/home/torrien/Pictures/Screenshot from 2020-08-02 19-36-00.png"
# FILE_PATH = "/home/torrien/Pictures/Screenshot from 2020-08-02 19-40-48.png"
# FILE_PATH = "/home/torrien/Pictures/Screenshot from 2020-08-02 20-23-17.png"
# FILE_PATH = "/home/torrien/Pictures/Screenshot from 2020-08-02 21-01-32.png"
FILE_PATH = "test.jpg"
NEW_FN = f'test upload  by.png'

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# Step 2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_2 = {
    "action": "login",
    "lgname": WIKI_BOT_USER,
    "lgpassword": WIKI_BOT_PASS,
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

# Step 3: Obtain a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Post request to upload a file directly
PARAMS_4 = {
    "action": "upload",
    "filename": NEW_FN,
    "format": "json",
    "token": CSRF_TOKEN,
    "ignorewarnings": 1,
    # Comment holds the page text. Should include any templates and sections.
    # ==Section==
    # ===Subsection===
    # ====Sub-subsection====
    "comment": """==Description==
Test upload small screenshot 5. 
==Summary==
===Metadata===
{{Information
|Description=Just a small screenshot
|Date='2020-08-02'
|Source=apa.ebeltran.me
|Author='Torrien'
|Permission='Use as you please. No restrictions.'
}}"""
    # "tags":"description=Just a small screenshot|date=2020-08-02|source=apa.ebeltran.me|author=Torrien|permission=Use as you please. No restrictions.",

}

FILE = {'file':(NEW_FN, open(FILE_PATH, 'rb'), 'multipart/form-data')}

R = S.post(URL, files=FILE, data=PARAMS_4)
print("\n\n", R.text, "\n\n\n",)
DATA = R.json()
print(DATA)

S.close()
