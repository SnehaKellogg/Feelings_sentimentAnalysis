import os
from pathlib import Path

import pandas as pd
import numpy as np
import pickle
from sklearn.externals import joblib
# from twitterscraper.kill import scrape_tweets

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, request
# import newsapi
# from newsapi.newsapi_client import NewsApiClient


app = Flask(__name__, static_url_path='/static')

# location = '/static'
# fullpath = os.path.join(location, 'tweet.pkl')
# model = joblib.load(fullpath)
# model=joblib.load('tweet.pkl')


@app.route("/")
# ,methods=['GET'])
def index():
    # """Return the homepage."""
    return render_template("index.html")
    # searchinput = request.args.get('text-input','')
    # return searchinput

# @app.route("/", methods=['GET'])
# def searchword():
    


# @app.route('/', methods=['POST'])
# def my_form_post():
#    text = request.form['text']
#    input_text = text.upper()
#    return input_text

# 

@app.route("/bubblecloud")
def bubblecloud():
    # """Return the homepage."""
    return render_template("index_bubble.html")

@app.route("/news")
# /v2/top-headlines
def news():
    return render_template("news.html")
    

@app.route("/sidebar")
def nav():
    return render_template("sidebar.html")

@app.route("/bubbles")
def bubbles():
    return render_template("index1.html")


@app.route("/map")
def worldmap():
    # """Return the homepage."""
    return render_template("Worldmap.html")

@app.route("/twitterstats")
def twitterstats():
    # """Return the homepage."""
    return render_template("whytwitter.html")

@app.route("/team")
def team():
    # """Return the homepage."""
    return render_template("team.html")

# @app.route("/scrape")
# def 


if __name__ == "__main__":
    app.run()
# port = int(os.environ.get("PORT", 5000))
# app.run(host='0.0.0.0', port=port)
