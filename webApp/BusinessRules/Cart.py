class Cart:
    def __init__(self, userId):
        self.statusCodes = [
            "No items",
            "Waiting for checkout",
            "Paid"
        ]
        self.userId = userId
        self.itemsAmount = 0
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
        self.itemsAmount += 1
        self.status = self.statusCodes[1]

    def removeItem(self):
        pass

    def updateItemAmount(self, vendor, size, method):
        if vendor in self.items and size in self.items[vendor]["sizes"]:
            updateMode = 1 if method == "inc" else -1
            self.items[vendor]["sizes"][size] += updateMode
            self.itemsAmount += updateMode
            self.totalOrderPrice += updateMode * self.items[vendor]["price"]

    def confirmOrderAndSendRequest(self):
        # confirm ...
        self.status = self.statusCodes[2]

    def getCart(self):
        pass
