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
  results = db.episodes.find({ "season": season, "number": number })
  #formatting printed results
  print("Season: {}  Episode: {}".format(season, number))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Episode Title: {}".format(x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available.")
    else:
      print(x["summary"][3:-4] + "\n")

#findEpisode(1, 1)

def findSeason(season):
  '''All episodes from specified season.'''
  results = db.episodes.find({ "season": season })
  #formatting printed results
  print("Season: {}".format(season))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Episode {}:  {}".format(x["number"], x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available." + "\n")
    else:
      print(x["summary"][3:-4] + "\n")

#findSeason(1)
#findSeason(2)

def onAir(airdate):
  '''Episode from the specified airing date.'''
  results = db.episodes.find({ "airdate": airdate })
  #formatting printed results
  print("Given Date: {}".format(airdate))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Season {} Episode {}: {}".format(x["season"], x["number"], x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available." + "\n")
    else:
      print(x["summary"][3:-4] + "\n")

#onAir("2001-03-06")

def findWords(key):
  keyword = ".*" + key + ".*"
  results = db.episodes.find({"summary": {"$regex": keyword }})
  #formatting printed results
  print("Key Word: {}".format(key))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Season: {}  Episode: {}".format(x["season"], x["number"]))
    print("Episode Title: {}".format(x["name"]))
    print(x["summary"][3:-4] + "\n")

#findWords("Sandy Cheeks")
#findWords("Squidward")


print("------ Find an episode by giving a season and episode number. ------")
season = input("Please enter a season: ")
number = input("Please enter an episode number: ")
while(not season.isnumeric()):  #checking for non-numbers
  season = input("Please enter a valid number: ")
while(not number.isnumeric()):
  number = input("Please enter a valid number: ")
print()

findEpisode(int(season),int(number))

print("------ Find episode(s) aired on a given date. ------")
year = input("Please enter a four-year between 1999 and 2020: ")
while(not year.isnumeric() or (int(year) > 2020) or (int(year) < 1999)):  #checking for valid years
  year = input("Please enter a valid four-digit year: ")
month = input("Please enter a month (with a 0 in front of single-digit months): ")
while(not(len(month) == 2) or not month.isnumeric() or int(month) > 12 or int(month) < 1):  #checking for valid month (with the 0)
  month = input("Please enter a valid month (with a 0 in front of single-digit months): ")
day = input("Please enter a day (with a 0 in front of single-digit days): ")
while(not day.isnumeric() or not(len(day) == 2) or int(day) > 31 or int(day) < 1):  #checking for valid dates (with the 0)
  day = input("Please enter a valid day (between 1 and 31, and with a 0 in front of single-digit days): ")
print()

onAir(year + "-" + month + "-" + day)

print("------ Find episodes with the given key words or phrases. ------")
word = input("Please enter key words: ")
print()

findWords(word)
