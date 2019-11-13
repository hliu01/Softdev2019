#Henry Liu
#SoftDev1 pd9
#K24: A RESTful Journey Skyward
#2019-11-12


from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)

@app.route("/")
def root():

    url = "https://pokeapi.co/api/v2/pokemon/"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data= json.loads(response.data)
    return render_template("index.html",  abilities = data['1'])

@app.route("/taco")
def taco():
        url2 = "http://taco-randomizer.herokuapp.com/random/"
        response2 = http.request('GET', url2)
    data2= json.loads(response2.data)
        return render_template("index.html",  abilities = data['1'])



if __name__ == "__main__":
    app.debug = True
    app.run()
