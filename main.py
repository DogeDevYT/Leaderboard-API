from art import *
from colorama import init
from util import printUtil
from config import configReader
from reading import mongodbReader
from output import textfileOutput
from output import websiteOutput

# Initialize colorama on Windows
init()

# Create ASCII art banner with colored text
ascii_art = text2art("Leaderboard-API")
printUtil.print_text_in_green(ascii_art)

printUtil.print_text_in_green(f"Starting Leaderboard-API...")

# read config file and store config
config = configReader.read_config()

ranking_method = config["ranking"]["top"]
count = config["ranking"]["count"]

if config["db"] == "mongodb":
    leaderboard_data = mongodbReader.readMongodb(ranking_method, count)
    printUtil.print_text_in_green(f"Successfully read {ranking_method} {count} from {config['db']}")

if config["output"] == "textfile":
    textfileOutput.write_to_text_file(leaderboard_data)
    printUtil.print_text_in_green(f"Successfully wrote leaderboard data to output/leaderboard.txt")
elif config['output'] == 'website':
    websiteOutput.write_leaderboard_website(leaderboard_data)
    printUtil.print_text_in_green(f"Successfully wrote leaderboard data to output/leaderboard.html")
