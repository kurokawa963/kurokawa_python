
# G's ACADEMY TOKYOからメンター画像を取得

import os
from urllib. request import urlopen
from pprint import pprint
from bs4 import BeautifulSoup

# メンター一覧ページのHTML
with urlopen("https://gsacademy.jp/mentor-lecturer") as res:
    html=res.read().decode("utf-8")

# BeautifulSoupインスタンスを生成
soup=BeautifulSoup(html, "html.parser")

#画像URL一覧を作成
img_urls=[e["src"]for e in soup.select(".mentor__list img")]
#リスト内包表記

# 「http://～」の形式に変換
img_urls=[u if u.find("http")==0 else "https://gsacademy.jp"+ u for u in img_urls]

# 保存先のディレクトリを作成します
if not os.path.exists("img"):
    os.mkdir("img")

#画像を読み込んでディレクトリに保存
for i,url in enumerate(img_urls):
    print(i, url)
    with urlopen(url) as res:
        img= res.read()
        with open("img/%d.png" % (i+1),"wb") as f:
            f.write(img)