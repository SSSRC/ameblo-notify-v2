import requests
import re
import pandas as pd
from utils.post2slack import post2slack
from utils.getTitleFromURL import getTitleFromURL
from utils.post2twitter import post2twitter
import os
import json
from dotenv import load_dotenv
load_dotenv()

subteam_id = os.getenv("SUBTEAM_ID")
if subteam_id == None:
   subteam_id=""

# 簡易スクレイピング
base_url = "https://ameblo.jp"
entrylist_url = base_url + "/sssrc/entrylist.html"
html_content = requests.get(entrylist_url)
urls = re.findall(r'/sssrc/entry-\d{11}.html', html_content.text)
print(len(set(urls)))

# IdとURLの辞書作成
entry_id = {}
for path in set(urls):
  entry_id[int(path[13:24])] = base_url + path

# 既存データベースの取得
try:
  df = pd.read_csv("data/data.csv")
  print("データをロードしました")
  print(df)
  ids = set(df["id"]) #setにすることで計算量が(以下略)
except FileNotFoundError:
  print("データがありません")
  df = pd.DataFrame(index=[], columns=["id","url"])
  ids = set()

# 既存のデータベースとの参照、Slackで通知
for id in entry_id:
  if id in ids:
    pass
  else:
    url = entry_id[id]
    tweet_url = "https://twitter.com/intent/tweet?url=" + url
    print("新規投稿:",url,", TweetURL:",tweet_url)
    # Twitter自動投稿
    title = getTitleFromURL(url)
    tweet_msg = 'アメブロを投稿しました！\n\n' + title + '\n⇨ ' + url
    posted_url = post2twitter(tweet_msg)
    # Slack投稿テンプレート
    if posted_url != None:
        msg = "アメブロに新規投稿がありました\nURL:" + url + "\n\nTwitterへ自動投稿されました．\n" + posted_url
    else:
        msg = "<!subteam^"+ subteam_id +">\nアメブロに新規投稿がありました\nURL:" + url + "\n\nTwitterへの自動投稿に失敗したので下記の文面をコピーしてTwitterへ投稿を行ってください．\n-----------------------\n" + tweet_msg
    post2slack(msg)
    df = pd.concat([df, pd.DataFrame({'id': [id], 'url': [url]})], ignore_index=True)
    # break # デバッグ用

# 出力
df.to_csv("data/data.csv",index=False)