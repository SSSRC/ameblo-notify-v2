import os
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
load_dotenv()
# 説明
print("API_KEYとAPI_KEY_SECRETを用い、\nACCESS_TOKENとACCESS_TOKEN_SECRETを発行します。")
# セットアップ
api_key = os.getenv("API_KEY")
if api_key == None:
    print("環境変数にAPI_KEYがありません。入力してください。")
    api_key = input(">")
    print("")
api_key_secret = os.getenv("API_KEY_SECRET")
if api_key == None:
    print("環境変数にAPI_KEYR_SECRETがありません。入力してください。")
    api_key_secret = input(">")
    print("")

# tokenを要求
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(api_key, client_secret=api_key_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "api_key か api_key_secret にエラーがあります"
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")

# 認可URLの発行
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("連携するTwitterアカウントでログインした上で、リンクにアクセスして認証してください。")
print(authorization_url)
verifier = input("PINを入力してください: ")

# PINの検証とtokenの取得
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    api_key,
    client_secret=api_key_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]
print("====tokenが発行されました====")
print("access_token")
print(access_token)
print("access_token_secret")
print(access_token_secret)
with open(".token", mode='w') as f:
    f.write("ACCESS_TOKEN="+access_token +"\nACCESS_TOKEN_SECRET="+access_token_secret)
print(".tokenにも保存しました")
