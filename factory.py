# Abstract Product
class Pizza:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name} pizza")

    def bake(self):
        print(f"Baking {self.name} pizza")

    def cut(self):
        print(f"Cutting {self.name} pizza")

    def box(self):
        print(f"Boxing {self.name} pizza")

class CheesePizza(Pizza):
    def __init__(self):
        super().__init__("cheese")

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("pepperoni")

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")

class PizzaStore:
    @staticmethod
    def order_pizza(pizza_type):
        pizza = PizzaFactory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

PizzaStore.order_pizza("cheese")
PizzaStore.order_pizza("pepperoni")
