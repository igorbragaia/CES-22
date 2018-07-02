class Mediator:
    def __init__(self):
        self._class1 = Class1(self)
        self._class1 = Class2(self)


class Class1:
    def __init__(self, mediator):
        self._mediator = mediator


class Class2:
    def __init__(self, mediator):
        self._mediator = mediator


if __name__ == "__main__":
    mediator = Mediator()
