from util import printUtil

import json
import os

def read_config():
    data = {}
    #load data from config file
    printUtil.print_text_in_green(f"Reading config.json...")
    #create config dictionary to be used for later
    config_settings = {}
    try:
        #read from /config/config.json
        config_file_path = os.path.join('config', 'config.json')
        with open(config_file_path, 'r') as config_file:
            data = json.load(config_file)
    except FileNotFoundError as e:
        printUtil.print_text_in_red(f"Config File Not Found at /config/config.json! Exiting...")

    if data['database-type'] == 'mongodb':
        printUtil.print_text_in_green(f"Reading from mongodb database...")
        config_settings.update({"db": "mongodb"})
    else:
        printUtil.print_text_in_red(f"Unrecognized/Unsupported Database Type! Exiting...")
        exit(1)

    if data['ranking']['top'] == 'highest':
        count = data['ranking']['count']
        printUtil.print_text_in_green(f"Reading top {data['ranking']['count']} from database...")
        config_settings.update(
        {   "ranking":
            {
                "top": "highest",
                "count": count
            }
        })
    else:
        printUtil.print_text_in_red(f"Unsupported Ranking System! Exiting...")
        exit(1)

    outputFormat = data['output']

    if outputFormat == 'textfile' or outputFormat == 'txt':
        printUtil.print_text_in_green(f"Outputting the leaderboard data to a text file...")
        config_settings.update({"output": "textfile"})
    elif outputFormat == 'website':
        printUtil.print_text_in_green(f"Outputting the leaderboard data to a static HTML website...")
        config_settings.update({"output": "website"})
    else:
        printUtil.print_text_in_red(f"Unsupported Output Format! Exiting...")
        exit(1)
    return config_settings