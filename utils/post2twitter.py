from requests_oauthlib import OAuth1Session
import os
import json
from dotenv import load_dotenv
load_dotenv()


def post2twitter(msg):
    payload = {"text": msg}
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    twitter_id = os.getenv("TWITTER_ID")
    try:
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )
        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text)
            )
        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))
        return "https://twitter.com/" + twitter_id + "/status/" + json_response["data"]["id"]
    except:
      # TODO原因分岐
      return None


if __name__ == "__main__":
    print(post2twitter("投稿テスト"))