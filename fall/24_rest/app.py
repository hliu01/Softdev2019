#Henry Liu
#SoftDev1 pd9
#K24: A RESTful Journey Skyward
#2019-11-12

from flask import Flask, render_template
import urllib.request as urllib
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=XVA4sqATNDCNJfAqfACjHrpzBNOgvWeaMsdH9W5z")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic = data['url'], explanation = data['explanation'])

if __name__ == "_main_":
    app.debug = True
    app.run()
