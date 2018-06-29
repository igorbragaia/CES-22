import abc


class Person(object):
    __metaclass__ = abc.ABCMeta

    default_abilities = ['walking', 'speaking']

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    @classmethod
    @abc.abstractmethod
    def abilities(cls):
        """Returns habilites list"""
        return cls.default_abilities

    @staticmethod
    def flag():
        return "this method is independent from this class"

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    @abc.abstractmethod
    def name(self):
        pass


class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.profession = "student"
        self.__abilities = []

    @property
    def name(self):
        return "student " + self.firstName + " " + self.lastName

    @property
    def abilities(self):
        return self.default_abilities + self.__abilities

    @abilities.setter
    def abilities(self, ability):
        self.__abilities.extend(ability)


class Professor(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.profession = 'professor'
        self.__abilities = []

    @property
    def name(self):
        return "professor " + self.firstname + " " + self.lastname

    @property
    def abilities(self):
        return self.default_abilities + self.__abilities

    @abilities.setter
    def abilities(self, ability):
        self.abilities.extend(ability)


student1 = Student("Igor", "Bragaia")
professor1 = Professor("Luis", "Cláudio")
student1.abilities = ["teaching", "singing"]

print(student1.name)
print(student1.abilities)
print(professor1.abilities)
print(Person.flag())
print(Person.abilities())
