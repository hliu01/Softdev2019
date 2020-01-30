#Henry Liu and Kenneth Chin
#SoftDev1 pd9
#K24: A RESTful Journey Skyward
#2019-11-12

from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")

@app.route("/pokeapi")
def pokeapi():
    url = "https://pokeapi.co/api/v2/pokemon/"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data= json.loads(response.data)
    return render_template("pokeapi.html", name = data['name'],
        number = data['game_indices'][1]['game_index'],
        ability1 = data['abilities'][1]['ability']['name'],
        ability2 = data['abilities'][0]['ability']['name'])

@app.route("/taco")
def taco():
        url = "http://taco-randomizer.herokuapp.com/random/"
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        data= json.loads(response.data)
        food = data["condiment"]
        return render_template("index.html", name = food["name"], recipe = food["recipe"])

@app.route("/bike")
def bike():
        url = "http://api.citybik.es/v2/networks/nu-connect"
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        data= json.loads(response.data)
        data = data['network']
        location = data['location']
        company = data["company"]
        return render_template("bike.html", name = company[0],
                            city = location['city'],
                            country = location['country'],
                            latitude = location['latitude'],
                            longitude = location['longitude'],
                            nm = data['name'])




if __name__ == "__main__":
    app.debug = True
    app.run()
