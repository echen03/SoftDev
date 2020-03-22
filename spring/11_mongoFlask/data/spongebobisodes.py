#Team Eggcellent: Tiffany Cao & Ethan Chen
#SoftDev2 pd1
#K10: Import/Export Bank
#2020-02-29

from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.eggcellent

#The data bank used was the Spongebob Squarepants (SBSP) Episodes dataset from TV Maze API.
#This file provides numerous details about every SBSP episode in all the seasons, including episode summary, airtime, airdate, and more.
#The link to the API is: http://www.tvmaze.com/api
#The link to the JSON file for Spongebob Squarepants episodes is: http://api.tvmaze.com/singlesearch/shows?q=spongebob-squarepants&embed=episodes

#For the import mechanism, we used the curl tool for the url to create a JSON file.
#Using bson.json_util, we passed the file through the reader and inserted the contents to a collection called info.
#Because the JSON file consisted of only one extremely long line and was not formatted properly, we treated the document like a dictionary to get
#to the episodes which was in a long list. We then inserted every episode's information as a document in another collection named episodes.

info = db.info
with open("spongebob.json", "r") as file:  #read in json data
  content = file.readlines()
  if (info.count() == 0):
    for line in content:  #insert single line
      info.insert_one(loads(line))
    for x in info.find({}):
      temp = x["_embedded"]["episodes"]
      for y in temp:  #insert every episode's information
        db.episodes.insert_one(y)

def findEpisode(season, number):
  '''Episode name from the specified season and episode number.'''
  episodes = db.episodes.find({ "season": season, "number": number })
  results = "Season {}, Episode {} \n".format(season, number);
  if (episodes.count() == 0):
      results += "Episode not available."
      return results
  for x in episodes:
    results += "Episode Title: {} \n \n".format(x["name"])
    if(x["summary"] == "" or x["summary"] is None):
      results += "No summary available."
    else:
      results += x["summary"][3:-4] + "\n"
  return results

def findSeason(season):
  '''All episodes from specified season.'''
  episodes = db.episodes.find({ "season": season })
  results = "Season: {}\n".format(season)
  if (episodes.count() == 0):
      results += "Season not available."
      return results
  results += "Total Episodes: {}\n \n".format(episodes.count())
  for x in episodes:
    results += "Episode {}:  {} \n".format(x["number"], x["name"])
    if(x["summary"] == "" or x["summary"] is None):
      results += "No summary available. \n \n"
    else:
      results += x["summary"][3:-4] + "\n \n"
  return results


def onAir(airdate):
  '''Episode from the specified airing date.'''
  episodes = db.episodes.find({ "airdate": airdate })
  results = "Given Date: {}\n".format(airdate)
  if (episodes.count() == 0):
      results += "No episode aired on this date.\n"
      return results
  results += "Total Episodes: {}\n \n".format(episodes.count())
  for x in episodes:
    results += "Season {}, Episode {}: {}\n".format(x["season"], x["number"], x["name"])
    if(x["summary"] == "" or x["summary"] is None):
      results += "No summary available. \n \n"
    else:
      results += x["summary"][3:-4] + "\n \n"
  return results

def findWords(key):
  keyword = ".*" + key + ".*"
  episodes = db.episodes.find({"summary": {"$regex": keyword }})
  results = "Key Word: {}\n".format(key)
  if (episodes.count() == 0):
      results += "No episode with this keyword was found.\n"
      return results
  results += "Total Episodes Found: {}\n \n".format(episodes.count())
  for x in episodes:
    results += "Season: {}, Episode {}\n".format(x["season"], x["number"])
    results += "Episode Title: {}\n".format(x["name"])
    if(x["summary"] == "" or x["summary"] is None):
      results += "No summary available. \n \n"
    else:
      results += x["summary"][3:-4] + "\n \n"
  return results
