# getter.py
from pyfacebook import Api
import config
import json

def get_data(appData):
    api = Api(
        app_id=appData.APP_ID,
        app_secret=appData.APP_SECRET,
        long_term_token=appData.ACCESS_TOKEN,
    )
    data = api.get_page_posts(
        page_id=page_username,
        since_time="2020-05-01",
        count=None,
        limit=100,
        return_json=True,
    )
    return data

def dump(data):
    with open("wto_posts.json", 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":

    page_username = "noise-bot432"

    appData = config.get_config(page_username)
    print("config data: "+str(appData))
    page_data = get_data(appData)
    print("page data: "+str(page_data))
  