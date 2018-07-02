from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    def __init__(self):
        self.id = 1

    @abstractmethod
    def metodo(self):
        pass


class Exemplo(Base):
    def __init__(self):
        super().__init__()

    def metodo(self):
        pass


if __name__ == "__main__":
    Exemplo()