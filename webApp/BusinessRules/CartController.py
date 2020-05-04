from . import Cart

class CartController:
    def __init__(self):
        pass

    def generateCart(self, userId):
        cartInstance = Cart.Cart(userId)

        return cartInstance