from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car is stopping.")

    def drive(self):
        print("The car is driving.")

class Truck(Vehicle):
    def start(self):
        print("The truck is starting.")

    def stop(self):
        print("The truck is stopping.")

    def drive(self):
        print("The truck is driving.")

class Bus(Vehicle):
    def start(self):
        print("The bus is starting.")

    def stop(self):
        print("The bus is stopping.")

    def drive(self):
        print("The bus is driving.")

car = Car('Ford', 'SX', 'blue')
truck = Truck('Volvo', 'VNX', 'grey')
bus = Bus('Mercedes', 'OC', 'white')

vehicles = [car, truck, bus]

for v in vehicles:
    v.start()
    v.stop()
    v.drive()
    print()