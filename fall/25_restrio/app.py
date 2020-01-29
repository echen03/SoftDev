from flask import Flask, render_template, request, redirect, url_for
import urllib.request, json
import random
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/weather")
def weather():
    u = urllib.request.urlopen("https://www.metaweather.com/api/location/2459115")
    response = u.read()
    data = json.loads(response)
    return render_template("weather.html", weather = data['consolidated_weather'])

@app.route("/unsplash")
def unsplash():
    u = urllib.request.urlopen("https://api.unsplash.com/photos/random?client_id=ca71347b01435c6083ec9d29b381d8eedf67d11e85c41177a2183a0d9236a4be")
    response = u.read()
    data = json.loads(response)
    description = data['description']
    return render_template("unsplash.html", pic = data['urls']['small'], description = description, likes = data['likes'], user = data['user']['name'])

@app.route("/met")
def met():
    u = urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/999")
    response = u.read()
    data = json.loads(response)
    return render_template("met.html", pic = data['primaryImageSmall'], title = data['title'], department = data['department'], medium = data['medium'], obj_date = data['objectDate'], country = data['country'])

@app.route("/countries", methods = ['GET'])
def countries():
        if ("country" in request.args):
            country = request.args["country"]
            try:
                u = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/" + country.replace(" ", "%20"))
                response = u.read()
                data = json.loads(response)
                list_of_languages = data[0]["languages"]
                languages = []
                #goes through the list of languages and retrieve the names of the languages
                for language in list_of_languages:
                    languages.append(language["name"])
                return render_template("index.html", name = data[0]['name'], alpha= data[0]['alpha2Code'], pop = data[0]['population'], languages = languages, currency = data[0]["currencies"][0]["name"])
            except:
                return redirect(url_for("root"))
        else:
            return render_template("index.html", name = "", alpha= "", pop = "")

@app.route("/countries2", methods = ['GET'])
def countries2():
        regions = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
        countries = []
        alpha2code = []
        alpha3code = []
        for region in regions:
            u = urllib.request.urlopen("https://restcountries.eu/rest/v2/region/" + region + "?fields=name;alpha2Code;alpha3Code")
            response = u.read()
            data = json.loads(response)
            for country in data:
                countries.append(country["name"])
                alpha2code.append(country["alpha2Code"])
                alpha3code.append(country["alpha3Code"])
        return render_template("index.html", countries = countries, alpha2code = alpha2code, alpha3code = alpha3code)

@app.route('/loripsum')
def loripsum():
    u = urllib.request.urlopen('https://loripsum.net/api/1/verylong/plaintext')
    response = u.read()
    #data = json.loads(response)
    return render_template('index.html', text = response)

@app.route('/nhl')
def nhl():
    u = urllib.request.urlopen('https://statsapi.web.nhl.com/api/v1/teams?teamId=4,5,6')
    response = u.read()
    data = json.loads(response)
    teamNames = []
    teamList = data["teams"]
    for t in teamList:
        teamNames.append(t["name"])
    return render_template('nhl.html', teams = teamNames)

@app.route('/quote')
def quote():
    u = urllib.request.urlopen('http://quotes.rest/qod.json')
    response = u.read()
    data = json.loads(response)
    quote = data["contents"]["quotes"][0]["quote"]
    author = data["contents"]["quotes"][0]["author"]
    return render_template('quote.html', quote = quote, author = author)


if __name__ == "__main__":
    app.debug = True
    app.run()
