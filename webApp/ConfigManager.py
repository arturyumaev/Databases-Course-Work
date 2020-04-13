import sqlite3


class ConfigManager():
    def __init__(self):
        self.configName = "./config.ini"

    def readConfig(self):
        try:
            self.config = open(self.configName, "r")
            self.configuration = self.config.readlines()
            self.db = self.configuration[0][9:-1]
            self.path = self.configuration[1][5:-1]

            if self.db == "sqlite3":
                self.api = sqlite3

        except IOError:
            print("An error occured while reading configuration file", self.configName)
            self.api = sqlite3
            self.path = "./database/catalog.db"
            print("Database configuration was set to default SQLite settings.")
        else:
            self.config.close()
        finally:
            return self.api, self.path



