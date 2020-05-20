import random

class OrdersManager:
    def __init__(self):
        pass

    def generateOrderNumber():
        orderNumber = "-".join(
            ["".join([str(n) for n in random.sample(range(10), 4)])
            for _ in range(2)]
        )

        return orderNumber