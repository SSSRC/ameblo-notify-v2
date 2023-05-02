import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def post2slack(msg):
  WEB_HOOK_URL = os.getenv("WEB_HOOK_URL") # SlackへのWebhook URL
  requests.post(WEB_HOOK_URL, data = json.dumps({
      'text': msg,  #通知内容
      'username': u'ameblo-notify',  #ユーザー名
      'icon_emoji': u':ameblo:',  #アイコン
      'link_names': 1,  #名前をリンク化
  }))

if __name__ == "__main__":
  post2slack("Slack投稿テスト")