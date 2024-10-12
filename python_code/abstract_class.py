#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod  # Abstract method
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print('The car is going.')


class Motorcycle(Vehicle):
    def go(self):
        print('The motorcycle is going.')


vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.go()
