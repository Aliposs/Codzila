class GameState:
    def __init__(self, level, score):
        self._level = level
        self._score = score

    def get_state(self):
        return (self._level, self._score)

class Game:
    def __init__(self):
        self._level = 1
        self._score = 0

    def play(self, level, score):
        self._level = level
        self._score = score

    def save(self):
        return GameState(self._level, self._score)

    def restore(self, memento):
        self._level, self._score = memento.get_state()

    def get_state(self):
        return (self._level, self._score)

class Caretaker:
    def __init__(self):
        self._saved_states = []

    def add_memento(self, memento):
        self._saved_states.append(memento)

    def get_memento(self, index):
        return self._saved_states[index]

game = Game()
caretaker = Caretaker()

game.play(2, 100)
caretaker.add_memento(game.save())

game.play(3, 200)
print(game.get_state())  # Output: (3, 200)

game.restore(caretaker.get_memento(0))
print(game.get_state())  # Output: (2, 100)
