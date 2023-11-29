from art import *
from colorama import init
from util import printUtil
from config import configReader
from reading import mongodbReader

# Initialize colorama on Windows
init()

# Create ASCII art banner with colored text
ascii_art = text2art("Leaderboard-API")
printUtil.print_text_in_green(ascii_art)

printUtil.print_text_in_green(f"Starting Leaderboard-API...")

#read config file and store config
config = configReader.read_config()

ranking_method = config["ranking"]["top"]
count = config["ranking"]["count"]

print(config)

print(mongodbReader.readMongodb(ranking_method, count))
#mongodbReader.readMongodb(config["ranking"]["top"], config["ranking"]["count"])