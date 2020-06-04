import sqlite3
import logging


class ConfigManager():
    def __init__(self):
        self.configName = "./config.ini"
        logging.basicConfig(filename='./applicationLog.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    def readConfig(self):
        try:
            logging.debug("Trying to establish connection")
            self.config = open(self.configName, "r")
            self.configuration = self.config.readlines()
            self.db = self.configuration[0][9:-1]
            self.path = self.configuration[1][5:-1]

            if self.db == "sqlite3":
                self.api = sqlite3

        except IOError:
            logging.error("An error occured while reading configuration file %s", self.configName)
            self.api = sqlite3
            self.path = "./database/catalog.db"
            logging.error("Database configuration was set to default SQLite settings.")
        else:
            logging.warning("Connection closed")
            self.config.close()
        finally:
            return self.api, self.path



