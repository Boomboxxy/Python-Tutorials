def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiply(self):
        return self.a*self.b

    def divide(self):
        return self.a / self.b
