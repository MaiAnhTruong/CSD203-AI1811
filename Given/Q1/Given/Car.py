class Car:
    def __init__(self, name="", price=-1):
        self.Name = name
        self.Price = price
    def __repr__(self):
        return f"({self.Name},{self.Price})"    