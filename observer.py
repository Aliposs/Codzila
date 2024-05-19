class Model:
    def __init__(self):
        self._observers = []
        self._data = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._data)

    def set_data(self, data):
        self._data = data
        self.notify()

class View:
    def update(self, data):
        print(f"View received data: {data}")

model = Model()
view = View()
model.attach(view)

model.set_data("New Data")
