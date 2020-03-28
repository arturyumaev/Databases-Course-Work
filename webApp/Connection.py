class Connection:
    def __init__(self, server):
        self.server = server
        self.instance = None
        self.configuration = None
    
    def getInstance(self):
        if self.server.__name__ == "sqlite3":

            with open("./db.conf", "r") as sqliteConfig:
                self.configuration = sqliteConfig.readline()
            
            try:
                self.instance = self.server.connect(self.configuration)

                return self.instance
            except IOError:
                print('An error occurred trying to connect to sqlite3')
        else:
            # Handling of other database servers may be added
            return None
