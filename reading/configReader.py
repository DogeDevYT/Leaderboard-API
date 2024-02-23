from util import printUtil
import json
import os

class ConfigReader:
    def __init__(self):
        self.printer = printUtil.TextPrinter()

    def read_config(self):
        config_settings = {}
        try:
            self.printer.print_text_in_color(f"Reading config.json...", "green")
            config_file_path = os.path.join('config', '../config/config.json')
            with open(config_file_path, 'r') as config_file:
                data = json.load(config_file)
        except FileNotFoundError as e:
            self.printer.print_text_in_color(f"Config File Not Found at /config/config.json! Exiting...", "red")

        if data['database-type'] == 'mongodb':
            self.printer.print_text_in_color(f"Reading from mongodb database...", "green")
            config_settings.update({"db": "mongodb"})
        elif data['database-type'] == 'postgresql' or data['database-type'] == 'postgres':
            self.printer.print_text_in_color(f"Reading from postgresql database...", "green")
            config_settings.update({"db": "postgresql"})
        else:
            self.printer.print_text_in_color(f"Unrecognized/Unsupported Database Type! Exiting...", "red")
            exit(1)

        if data['ranking']['top'] == 'highest':
            count = data['ranking']['count']
            self.printer.print_text_in_color(f"Reading top {count} from database...", "green")
            config_settings.update(
                {"ranking": {"top": "highest", "count": count}}
            )
        elif data['ranking']['top'] == 'lowest':
            count = data['ranking']['count']
            self.printer.print_text_in_color(f"Reading bottom {count} from database...", "green")
            config_settings.update(
                {"ranking": {"top": "lowest", "count": count}}
            )
        elif data['ranking']['top'] == 'time highest':
            count = data['ranking']['count']
            self.printer.print_text_in_color(f"Reading top {count} (time) from database...", "green")
            config_settings.update(
                {"ranking": {"top": "time highest", "count": count}}
            )
        elif data['ranking']['top'] == 'time lowest':
            count = data['ranking']['count']
            self.printer.print_text_in_color(f"Reading bottom {count} (time) from database...", "green")
            config_settings.update(
                {"ranking": {"top": "time lowest", "count": count}}
            )
        else:
            self.printer.print_text_in_color(f"Unsupported Ranking System! Exiting...", "red")
            exit(1)

        outputFormat = data['output']

        if outputFormat == 'textfile' or outputFormat == 'txt':
            self.printer.print_text_in_color(f"Outputting the leaderboard data to a text file...", "green")
            config_settings.update({"output": "textfile"})
        elif outputFormat == 'website':
            self.printer.print_text_in_color(f"Outputting the leaderboard data to a static HTML website...", "green")
            config_settings.update({"output": "website"})
        else:
            self.printer.print_text_in_color(f"Unsupported Output Format! Exiting...", "red")
            exit(1)

        return config_settings
