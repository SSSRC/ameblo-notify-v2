import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


def post2slack(msg):
    WEB_HOOK_URL = os.getenv("WEB_HOOK_URL")  # SlackへのWebhook URL
    try:
        response = requests.post(WEB_HOOK_URL, data=json.dumps({
            'text': msg,
            'username': u'ameblo-notify',
            'icon_emoji': u':ameblo:',
            'link_names': 1,
        }))
        if response.status_code == 200:
            print('Slackに投稿しました')
        else:
            print('Slackへの投稿に失敗しました')
            print(response.json())
    except Exception as e:
        print(f'Slackへの投稿に失敗しました: {e}')


if __name__ == "__main__":
    post2slack("Slack投稿テスト")
