from .ConfigManager import ConfigManager


class Connection():
    def __init__(self):
        self.getConfig()
        self.instance = None

    def getConfig(self):
        self.api, self.path = ConfigManager().readConfig()

    def getInstance(self):
        try:
            print("Trying to connect to database.")
            self.instance = self.api.connect(self.path)
        except:
            print("An error occured while connecting to database")
            print("Trying to reconnect...")
            for i in range(1, 4):
                print("Attempt to connect...", i)
                try:
                    self.instance = self.api.connect(self.path)
                except TimeoutError:
                    print("Can't connect.")
        finally:
            if self.instance == None:
                print("Couldn't connect to database")
                raise RuntimeError
            else:
                print("A connection to the database has been established")
                
                return self.instance


