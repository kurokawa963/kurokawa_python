
import os
from urllib. request import urlopen
from pprint import pprint
from bs4 import BeautifulSoup
from random import shuffle

with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

titles = soup.select("h3.entrylist-contents-title")
shuffle(titles)
title = titles[0]
print(title)
