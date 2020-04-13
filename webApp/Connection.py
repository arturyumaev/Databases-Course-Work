from .ConfigManager import ConfigManager


class Connection():
    def __init__(self):
        self.getConfig()

    def getConfig(self):
        self.api, self.path = ConfigManager().readConfig()

    def getInstance(self):
        return self.api.connect(self.path)