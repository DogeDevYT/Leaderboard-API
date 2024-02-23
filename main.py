from art import *
from colorama import init
from util import printUtil
from reading import mongodbReader, configReader, postgresqlReader
from output import leaderboardWriter as lbWriter

# Initialize colorama on Windows
init()

#Create our instances of all our Classes
writer = lbWriter.LeaderboardWriter()
config_reader = configReader.ConfigReader()
printer = printUtil.TextPrinter

# Create ASCII art banner with colored text
ascii_art = text2art("Leaderboard-API")
printer.print_text_in_color(ascii_art, "green")

printer.print_text_in_color(f"Starting Leaderboard-API...", "green")

#store config settings
config = config_reader.read_config()

ranking_method = config["ranking"]["top"]
count = config["ranking"]["count"]
db = config["db"]
output = config["output"]

if db == "mongodb":
    mongodb_reader_object = mongodbReader.MongodbReader()
    leaderboard_data = mongodb_reader_object.read_mongodb(ranking=ranking_method, count=count)
    printer.print_text_in_color(f"Successfully read {ranking_method} {count} from {db}", "green")
    print(leaderboard_data)
elif db == "postgresql":
    postgresql_reader_object = postgresqlReader.PostgresqlReader()
    leaderboard_data = postgresql_reader_object.read_postgresql_data(rankingMethod=ranking_method, count=count)
    printer.print_text_in_color(f"Successfully read {ranking_method} {count} from {db}", "green")
    print(leaderboard_data)

if output == "textfile":
    writer.write_to_text_file(leaderboard_data=leaderboard_data)
    printer.print_text_in_color(f"Successfully wrote leaderboard data to output/leaderboard.txt", "green")
elif output == 'website':
    writer.write_leaderboard_website(leaderboard_data=leaderboard_data)
    printer.print_text_in_color(f"Successfully wrote leaderboard data to output/leaderboard.html", "green")
