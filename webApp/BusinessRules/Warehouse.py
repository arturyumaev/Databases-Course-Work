import sys
sys.path.insert(0,'..')

from DatabaseStorage.SQLiteStorage import SQLiteStorage

class Warehouse:
    def __init__(self):
        self.databaseInstance = SQLiteStorage()

    def getItemsQuantity(self):
        data = self.databaseInstance.getItemsQuantity()

        return data

    def sendOrder(self, itemsDict):
        pass

    def _updateDatabase(self, itemsDict):
        pass

    def _deleteItemFromDatabase(self, vendor, quantity):
        pass

