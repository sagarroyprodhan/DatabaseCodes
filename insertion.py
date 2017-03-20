import pymongo
from pymongo import MongoClient
import json
import os

client = MongoClient('mongodb://admin:123@localhost:27017/')
db = client['youtube']
collection = db['test_collection']
path_to_json = 'test/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
index = 1
for js in json_files:
    page = open(path_to_json + js, 'r')
    parsed = json.loads(page.read())
    collection.insert(parsed)
    print(str(index) + ":" + parsed["videoInfo"]["snippet"]["title"])
    index = index + 1