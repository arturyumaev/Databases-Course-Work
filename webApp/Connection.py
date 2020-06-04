from ConfigManager import ConfigManager
import logging


class Connection():
    def __init__(self):
        self.getConfig()
        self.instance = None
        logging.basicConfig(filename='./applicationLog.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    def getConfig(self):
        self.api, self.path = ConfigManager().readConfig()
        logging.debug("Database API: %s", self.api)
        logging.debug("Database path: %s", self.path)

    def getInstance(self):
        try:
            logging.debug("Trying to connect to database.")
            self.instance = self.api.connect(self.path)
        except:
            logging.error("An error occured while connecting to database")
            logging.debug("Trying to reconnect...")
            
            for i in range(1, 4):
                logging.debug("Attempt to connect... %s", str(i))
                try:
                    self.instance = self.api.connect(self.path)
                except TimeoutError:
                    logging.error("Can not connect")
        finally:
            if self.instance == None:
                logging.error("Couldn't connect to database")
                raise RuntimeError
            else:
                logging.debug("A connection to the database has been established")
                
                return self.instance


