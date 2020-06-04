import logging
from . import Warehouse

class WarehouseController:
    def __init__(self):
        logging.basicConfig(filename='../applicationLog.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    def createWarehouseInstance(self):
        logging.debug("A new warehouse instance was created")
        return Warehouse.Warehouse()
