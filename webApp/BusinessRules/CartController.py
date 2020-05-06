
import redis
import pickle
from . import Cart

class CartController:
    def __init__(self):
        self.storageInstance = redis.Redis('localhost', port=6379, db=0)
        
    def generateCart(self, userSessionId):
        cartInstance = Cart.Cart(userSessionId)
        self.storageInstance.set(userSessionId, pickle.dumps(cartInstance))
    
    def getCart(self, userSessionId):
        cart = pickle.loads(self.storageInstance.get(userSessionId))

        return cart

    def updateCart(self, userSessionId, cart):
        self.storageInstance.set(userSessionId, pickle.dumps(cart))
