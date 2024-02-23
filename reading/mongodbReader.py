import pymongo
from pymongo import MongoClient
from util import printUtil
import json
import os

class MongodbReader:
    def __init__(self):
        self.results = {}
        self.client = None
        self.printer = printUtil.TextPrinter

    def _update_leaderboard_dict(self, mongoDBCursor, nameToDisplay):
        counter = 1
        for document in mongoDBCursor:
            self.results.update({counter: document[nameToDisplay]})
            counter += 1

    def read_mongodb(self, ranking, count):
        try:
            config_file_path = os.path.join('config', 'mongodbConfig.json')
            with open(config_file_path, 'r') as config_file:
                data = json.load(config_file)
        except FileNotFoundError as e:
            self.printer.print_text_in_color("Config File for MongoDB Not Found at /config/mongodbConfig.json! Exiting...", "red")
            exit(1)

        database = data["database"]
        collection = data["collection"]
        comparing_field = data["comparingField"]
        name_to_display = data["nameToDisplay"]

        uri = data["uri"]

        try:
            self.client = MongoClient(uri)
            db = self.client[database]
            accessed_collection = db[collection]

            if ranking == "highest":
                cursor = accessed_collection.find({}, {"_id": 0}).sort(comparing_field, pymongo.DESCENDING).limit(count)
                self._update_leaderboard_dict(mongoDBCursor=cursor, nameToDisplay=name_to_display)
            elif ranking == "lowest":
                cursor = accessed_collection.find({}, {"_id": 0}).sort(comparing_field, pymongo.ASCENDING).limit(count)
                self._update_leaderboard_dict(mongoDBCursor=cursor, nameToDisplay=name_to_display)
            elif ranking == 'time highest':
                cursor = accessed_collection.find().sort(comparing_field, pymongo.DESCENDING).limit(count)
                self._update_leaderboard_dict(mongoDBCursor=cursor, nameToDisplay=name_to_display)
            elif ranking == 'time lowest':
                cursor = accessed_collection.find().sort(comparing_field, pymongo.ASCENDING).limit(count)
                self._update_leaderboard_dict(mongoDBCursor=cursor, nameToDisplay=name_to_display)
            else:
                self.printer.print_text_in_color(f"Unsupported Ranking System for MongoDB! Exiting...", "red")
                exit(1)
        except Exception as e:
            self.printer.print_text_in_color("Connection to MongoDB failed: " + str(e), "red")
        finally:
            self.client.close()
        return self.results
# sample connction string:
# uri = "mongodb+srv://<username>:<password>@thecluster.pm9jkpk.mongodb.net"