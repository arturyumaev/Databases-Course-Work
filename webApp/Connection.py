from .ConfigManager import ConfigManager


class Connection():
    def __init__(self):
        self.getConfig()
        self.instance = None

    def getConfig(self):
        self.api, self.path = ConfigManager().readConfig()
        print("LOG: Database API:", self.api)
        print("LOG: Database path:", self.path)

    def getInstance(self):
        try:
            print("LOG: Trying to connect to database.")
            self.instance = self.api.connect(self.path)
        except:
            print("LOG: An error occured while connecting to database")
            print("LOG: Trying to reconnect...")
            for i in range(1, 4):
                print("LOG: Attempt to connect...", i)
                try:
                    self.instance = self.api.connect(self.path)
                except TimeoutError:
                    print("LOG: Can't connect.")
        finally:
            if self.instance == None:
                print("LOG: Couldn't connect to database")
                raise RuntimeError
            else:
                print("LOG: A connection to the database has been established")
                
                return self.instance


