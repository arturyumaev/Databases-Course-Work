import random
import sys
import logging
from time import gmtime, strftime
sys.path.insert(0,'..')

from DatabaseStorage.SQLiteStorage import SQLiteStorage


class OrdersManager:
    def __init__(self):
        logging.basicConfig(filename='../applicationLog.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    def generateOrderNumber(self):
        orderNumber = "-".join(
            ["".join([str(n) for n in random.sample(range(10), 4)])
            for _ in range(2)]
        )

        return orderNumber

    def createNewOrder(self, name, email, cart):
        logging.debug("A new order was created for %s, %s", name, email)
        
        orderNumber = self.generateOrderNumber()
        cartId = cart.cartId
        timeOrderCreated = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sqliteStorage = SQLiteStorage()

        for vendor in cart.items:
            for size in cart.items[vendor]['sizes']:
                quantity = cart.items[vendor]['sizes'][size]
                sqliteStorage.insertItemIntoOrders(
                    orderNumber, cartId, name, vendor, size, quantity, email, timeOrderCreated)