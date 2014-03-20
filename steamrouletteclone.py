from bs4 import BeautifulSoup as Soup
import json
import requests
from random import choice
from time import time

from flask import request, Flask

app = Flask(__name__)

@app.route("/getdata", methods=["GET"])
def getdata():
    try:
        soup = Soup(requests.get("http://steamcommunity.com/id/{id}/games?tab=all".format(id=request.args.get('id', ''))).text)
    except KeyError:
        return "No user ID provided"

    script = soup.findAll('script')[11].text
    data = json.loads(script.strip().split("\r\n")[0][14:-1])

    options = []

    for a in data:
        if "last_played" in a:
            if a["last_played"] < time()-604800:
                options.append(a)

    return "Play {name}: <a href=\"steam://play/{appid}\">Click here</a>".format(**choice(options))

app.run(host='0.0.0.0', port=7576)