from bs4 import BeautifulSoup as Soup
import json
import requests
from random import choice
from time import time
import ago
from datetime import datetime

from flask import request, Flask, make_response

app = Flask(__name__)

@app.route("/getdata", methods=["GET"])
def getdata():
    try:
        soup = Soup(requests.get("http://steamcommunity.com/id/{id}/games?tab=all".format(id=request.args.get('id', ''))).text)
    except KeyError:
        return "No user ID provided"

    try:
        script = soup.findAll('script')[11].text
    except IndexError:
        resp = make_response(json.dumps({"name": "Couldn't get Steam information", "appid": "0", "logo": "http://puushbrowse.blha303.com.au/broken.png"}))
        resp.headers["Access-Control-Allow-Origin"] = "http://steamroulette.blha303.com.au";
        return resp
    data = json.loads(script.strip().split("\r\n")[0][14:-1])

    options = []

    for a in data:
        if "last_played" in a:
            if a["last_played"] < time()-604800:
                a["since"] = ago.human(datetime.fromtimestamp(a["last_played"]))
                options.append(a)
        else:
            a["name"] += " <i>(never played)</i>"
            options.append(a)

    resp = make_response(json.dumps(choice(options)))
#    resp = make_response("Play {name}: <a href=\"steam://play/{appid}\">Click here</a><br><a href=\"steam://play/{appid}\"><img src=\"{logo}\" alt=\"{name}\">".format(**choice(options)))
    resp.headers["Access-Control-Allow-Origin"] = "http://steamroulette.blha303.com.au";
    return resp

app.run(host='0.0.0.0', port=7576, debug=True)
