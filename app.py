# https://flask.palletsprojects.com/en/2.0.x/quickstart/
from flask import Flask, render_template, request
import random
import requests
import time

app = Flask(__name__)

@app.route('/')
def home():
    # return "<p>Hello, test text dog!</p>"
    color = random.choice(['red','yellow','blue'])

    # panels = [
    #     "SuperHi API",
    #     "SuperHi Editor",
    #     "SuperHi Website"
    #     "BBC News"
    #     ]

    panels = [
        { "title": "Cargo", "url": "https://cargo.site/" },
        { "title": "Spline", "url": "https://spline.design/" },
        { "title": "Soundcloud", "url": "https://soundcloud.com/" },
        { "title": "Vice", "url": "https://www.vice.com/en" },
        { "title": "Coinbase", "url": "https://www.coinbase.com/" },
        { "title": "Smartly", "url": "https://www.smartly.io/" },
        { "title": "Youtube", "url": "https://www.youtube.com/" }
        ]

    return render_template("home.html", color=color, panels = panels)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/ping")
def ping():
    url = request.args.get("url")

    start_time = time.time()
    r = requests.get(url)
    end_time = time.time()

    diff_time = int((end_time - start_time) * 1000)

    return { 
        "url": url,
        "code": r.status_code, 
        "speed": diff_time 
        }