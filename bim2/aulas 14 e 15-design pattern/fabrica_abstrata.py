from abc import ABC, abstractmethod


class Base(ABC):
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


Exemplo()