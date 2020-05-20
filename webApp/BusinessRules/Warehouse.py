import sys
sys.path.insert(0,'..')

from DatabaseStorage.SQLiteStorage import SQLiteStorage

class Warehouse:
    def __init__(self):
        self.databaseInstance = SQLiteStorage()

    def getItemsQuantity(self):
        data = self.databaseInstance.getItemsQuantity()

        return data

    def removeOrderedItems(self, items):
        for vendor in items:
            for size in items[vendor]['sizes']:
                quantity = items[vendor]['sizes'][size]
                self.databaseInstance.updateItemQuantity(vendor, size, quantity)