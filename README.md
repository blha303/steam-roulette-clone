Steam Roulette Clone
====================

I went to use Steam Roulette the other day, and discovered that it didn't work. (on Chrome with Windows 8), so I figured, "How difficult could this be?" Turns out it's a cool challenge anyone can do in two hours.

Usage
-----

* `virtualenv venv -ppython2.7`
* `source bin/activate`
* `pip install -r requirements.txt`
* `python steamrouletteclone.py`
* Server starts on port 7576.
* Go to `http://hostname:7576/getdata?id=steamcommunityprofilename`, with `steamcommunityprofilename` as the last bit in a url like http://steamcommunity.com/id/blha303
* To set your Steam profile ID, here's the first Google result: http://www.lastlightforum.com/showthread.php?t=959

[Site source](https://github.com/blha303/steam-roulette-clone/tree/site)
