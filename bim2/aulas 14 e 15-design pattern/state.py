from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        pass


class ConcreteStateB(State):
    def handle(self):
        pass


if __name__ == "__main__":
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.request()
