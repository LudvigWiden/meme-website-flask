import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_meme():
    # Interact with reddit api
    #sr = "/wholesomememes"
    #url = "https://meme-api.herokuapp.com/gimme" + sr
    url = "https://meme-api.herokuapp.com/gimme"
    try:
        response = json.loads(requests.get(url).text)
        meme_large = response["preview"][-2]
        subreddit = response["subreddit"]
        return meme_large, subreddit
    except json.decoder.JSONDecodeError as error:
        return None, None


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic is None and subreddit is None:
        return "Error: Could not get data from API. Please try again later."
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


# Run on localhost, on port 5000
app.run(host="0.0.0.0", port=5000)
