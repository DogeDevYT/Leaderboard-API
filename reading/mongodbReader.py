import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from util import printUtil

import json
import os

# sample connction string:
# uri = "mongodb+srv://<username>:<password>@thecluster.pm9jkpk.mongodb.net"

def readMongodb(ranking, count):
    results = {}

    try:
        #read from /config/mongodbConfig.json
        config_file_path = os.path.join('config', 'mongodbConfig.json')
        with open(config_file_path, 'r') as config_file:
            data = json.load(config_file)
    except FileNotFoundError as e:
        printUtil.print_text_in_red(f"Config File for MongoDB Not Found at /config/mongodbConfig.json! Exiting...")
        exit(1)

    username = data["username"]
    password = data["password"]
    database = data["database"]
    collection = data["collection"]
    comparingField = data["comparingField"]
    nameToDisplay = data["nameToDisplay"]

    uri = f"{data['uri1']}{username}:{password}{data['uri2']}"

    try:
        # Create MongoDB client
        client = MongoClient(uri)

        # Access database
        db = client[database]

        # Access collection in database
        accessed_collection = db[collection]

        # handle selection of data + ranking
        if ranking == "highest":
            # Select top n amount of rows based of a field that is defined in mongoDBconfig.json to be compared for in order for natural ordering
            cursor = accessed_collection.find({}, {"_id": 0}).sort(comparingField, pymongo.DESCENDING).limit(count)

            # initialize counter variable
            counter = 1
            for document in cursor:
                # update results dictionary
                results.update({counter: document[nameToDisplay]})
                # update counter with next place
                counter += 1
    except Exception as e:
        printUtil.print_text_in_red("Connection to MongoDB failed: " + str(e))
    return results