from abc import ABCMeta, abstractmethod

class Component(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    def operation(self):
        self._component.operation()


class ConcreteDecoratorB(Decorator):
    def operation(self):
        self._component.operation()


class ConcreteComponent(Component):
    def operation(self):
        pass


if __name__ == "__main__":
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()
