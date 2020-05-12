import random

class Cart:
    def __init__(self, userId):
        self.statusCodes = [
            "No items",
            "Waiting for checkout",
            "Paid"
        ]
        self.cartId = "-".join(
            ["".join([str(n) for n in random.sample(range(10), 4)])
            for _ in range(4)]
        )
        self.userId = userId
        self.itemsQuantity = 0
        self.items = {}
        self.status = self.statusCodes[0]
        self.totalOrderPrice = 0

    def addItem(self, vendor, size, price):
        if vendor in self.items:
            if size in self.items[vendor]["sizes"]:
                self.items[vendor]["sizes"][size] += 1
            else:
                self.items[vendor]["sizes"][size] = 1
        else:
            self.items[vendor] = {
                "price": price,
                "sizes" : {
                    size: 1
                }
            }
        self.totalOrderPrice += price
        self.itemsQuantity += 1
        self.status = self.statusCodes[1]

    def removeItem(self, vendor, size, price):
        self.itemsQuantity -= self.items[vendor]["sizes"][size]
        self.totalOrderPrice -= self.items[vendor]["sizes"][size] * price
        del self.items[vendor]["sizes"][size]

    def updateItemAmount(self, vendor, size, method):
        if vendor in self.items and size in self.items[vendor]["sizes"]:
            updateMode = 1 if method == "inc" else -1
            self.items[vendor]["sizes"][size] += updateMode
            self.itemsQuantity += updateMode
            self.totalOrderPrice += updateMode * self.items[vendor]["price"]

        return self.items[vendor]["sizes"][size], self.itemsQuantity, self.totalOrderPrice

    def confirmOrderAndSendRequest(self):
        # confirm ...
        self.status = self.statusCodes[2]
