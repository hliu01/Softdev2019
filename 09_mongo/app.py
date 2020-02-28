#Henry Liu
#SoftDev1 pd9
#K24: A RESTful Journey Skyward
#2019-11-12


from pymongo import MongoClient
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

def convertJSONtoMongoDB(filename){
    f = open("primer-dataset.json","r")
    Info = json.load(f);

    }
