class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(f"{self.brand} {self.model}")

c1 = Car("Toyota", "Innova")
c1.show()
