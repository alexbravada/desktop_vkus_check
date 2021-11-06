

class Discount():
    def __init__(self, n):
        self.n = "0.0"
        self.n = float(n)

    def change(self, discount):
        self.n = float(discount)
        return self.n

    def value(self):
        return self.n

