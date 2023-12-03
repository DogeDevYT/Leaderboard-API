from util import printUtil
import psycopg2
import os
import json

class PostgresqlReader:
    def __init__(self):
        self.results = {}
        self.connection = ()
        self.printer = printUtil.TextPrinter
        self.config = {}

    def _add_rows_to_results_dict(self, rows, nameField, column_names):
        # get index of the name config field column
        name_index = column_names.index(nameField) if nameField in column_names else None

        if name_index is not None:
            counter = 1
            for row in rows:
                name = row[name_index]
                self.results.update({counter: name})
        else:
            self.printer.print_text_in_color("Incorrect name field for PostgreSQL reading! Quitting...", "red")
            exit(1)

    def _select_top_or_bottom_from_table(self, cursor, count, table_name, rankingMethod, comparingField, nameField):
        if rankingMethod == "highest":
            cursor.execute(f"SELECT * FROM {table_name} ORDER_BY {comparingField} DESC LIMIT {count}")
            rows = cursor.fetchall()
            # get column names
            column_names = [desc[0] for desc in cursor.description]
            self._add_rows_to_results_dict(rows=rows, nameField=nameField, column_names=column_names)
        elif rankingMethod == "lowest":
            cursor.execute(f"SELECT * FROM {table_name} ORDER_BY {comparingField} ASC LIMIT {count}")
            rows = cursor.fetchall()
            # get column names
            column_names = [desc[0] for desc in cursor.description]
            self._add_rows_to_results_dict(rows=rows, nameField=nameField, column_names=column_names)

    def read_postgresql_data(self, rankingMethod, count):
        try:
            config_file_path = os.path.join('config', 'postgresqlConfig.json')
            with open(config_file_path, 'r') as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError as e:
            self.printer.print_text_in_color("Config File for MongoDB Not Found at /config/mongodbConfig.json! Exiting...", "red")
            exit(1)

        dbname = self.config["dbname"]
        username = self.config["username"]
        password = self.config["password"]
        host = self.config["host"]
        port = self.config["port"]
        table_name = self.config["table"]
        comparing_field = self.config["comparingField"]
        name_field = self.config["name"]


        try:
            self.connection = psycopg2.connect(dbname=dbname,
                                               username=username,
                                               password=password, host=host,
                                               port=port)
            # make a cursor to execute SQL queries
            cursor = self.connection.cursor()
            self._select_top_or_bottom_from_table(cursor=cursor,
                                                  count=count,
                                                  table_name=table_name,
                                                  rankingMethod=rankingMethod,
                                                  comparingField=comparing_field,
                                                  nameField=name_field)
        except psycopg2.Error as e:
            self.printer.print_text_in_color(f"Error connecting to postgresql database {e}", "red")
        finally:
            self.connection.close()
        return self.results
