#builder design pattern
class Car:
    def __init__(self):
        self.model = None
        self.owner = None
        self.price = None

    def __str__(self):
        return f"Model: {self.model}Owner: {self.owner}Price: {self.price}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model

    def set_owner(self, owner):
        self.car.owner = owner

    def set_price(self, price):
        self.car.price = price

    def get_car(self):
        return self.car


if __name__ == "__main__":
    builder = CarBuilder()

    builder.set_model("Toyota Corolla \n")
    builder.set_owner("ali mohamed \n")
    builder.set_price(160000)

    car = builder.get_car()
    print(car)
