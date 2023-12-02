import pymongo
from pymongo import MongoClient
from util import printUtil
import json
import os

class MongodbReader:
    def __init__(self):
        self.results = {}
        self.client = None

    def read_mongodb(self, ranking, count):
        try:
            config_file_path = os.path.join('config', 'mongodbConfig.json')
            with open(config_file_path, 'r') as config_file:
                data = json.load(config_file)
        except FileNotFoundError as e:
            printUtil.print_text_in_red("Config File for MongoDB Not Found at /config/mongodbConfig.json! Exiting...")
            exit(1)

        username = data["username"]
        password = data["password"]
        database = data["database"]
        collection = data["collection"]
        comparingField = data["comparingField"]
        nameToDisplay = data["nameToDisplay"]

        uri = f"{data['uri1']}{username}:{password}{data['uri2']}"

        try:
            self.client = MongoClient(uri)
            db = self.client[database]
            accessed_collection = db[collection]

            if ranking == "highest":
                cursor = accessed_collection.find({}, {"_id": 0}).sort(comparingField, pymongo.DESCENDING).limit(count)
                counter = 1
                for document in cursor:
                    self.results.update({counter: document[nameToDisplay]})
                    counter += 1
        except Exception as e:
            printUtil.print_text_in_red("Connection to MongoDB failed: " + str(e))
        return self.results

    def close_connection(self):
        if self.client:
            self.client.close()

# sample connction string:
# uri = "mongodb+srv://<username>:<password>@thecluster.pm9jkpk.mongodb.net"