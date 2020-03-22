#Team Gray: Ethan Chen
#SoftDev2 pd1
#K11
#2020-03-05

from flask import Flask, render_template, request
from data import spongebobisodes
import json
from bson.json_util import loads
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html");

#findEpisode(1, 1)

@app.route("/findepisode")
def episode():
    season = int(request.args['season']);
    number = int(request.args['episode']);
    results = spongebobisodes.findEpisode(season, number);
    return render_template("results.html", results = results.split('\n'));

@app.route("/findseason")
def findSeason():
  season = int(request.args['season']);
  results = spongebobisodes.findSeason(season);
  return render_template("results.html", results = results.split('\n'));

@app.route("/findonAir")
def findonAir():
  airdate = request.args['year'] + "-" + request.args['month'] + "-" + request.args['day'];
  results = spongebobisodes.onAir(airdate);
  return render_template("results.html", results = results.split('\n'));

#onAir("2001-03-06")

@app.route("/findword")
def findWords():
  keyword = request.args['keyword']
  results = spongebobisodes.findWords(keyword);
  return render_template("results.html", results = results.split('\n'));

if __name__ == "__main__":
    app.debug = True
    app.run()
