# test.py
from pyfacebook import Api

APP_ID = "Your ID"
APP_SECRET = "Your SECRET"
ACCESS_TOKEN = "Your Token"


def get_data(page_username):
    api = Api(
        app_id=APP_ID,
        app_secret=APP_SECRET,
        long_term_token=ACCESS_TOKEN,
    )
    data = api.get_page_posts(
        page_id=page_username,
        since_time="2020-05-01",
        count=None,
        limit=100,
        return_json=True,
    )
    return data


def processor():
    page_username = "WHO"
    data = get_data(page_username)
    with open("wto_posts.json", 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    print("all set")