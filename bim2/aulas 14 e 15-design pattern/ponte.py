from abc import ABCMeta, abstractmethod


class AbstractInterface(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def someFunctionality(self):
        pass


class Bridge(AbstractInterface):
    def __init__(self):
        self.__implementation = None


class UseCase1(Bridge):
    def __init__(self, implementation):
        super().__init__()
        self.__implementation = implementation

    def someFunctionality(self):
        self.__implementation.anotherFunctionality()


class ImplementationInterface(metaclass=ABCMeta):
    @abstractmethod
    def anotherFunctionality(self):
        pass


class X(ImplementationInterface):
    def __init__(self):
        pass

    def anotherFunctionality(self):
        print("X")


class Y(ImplementationInterface):
    def __init__(self):
        pass

    def anotherFunctionality(self):
        print("Y")


if __name__ == "__main__":
    x = X()
    y = Y()

    usecase = UseCase1(x)
    usecase.someFunctionality()

    usecase = UseCase1(y)
    usecase.someFunctionality()
