class Person:
    def display(self):
        print("I am a person")

class Father(Person):
    def display(self):
        print("I am a father")

class Mother(Person):
    def display(self):
        print("I am a mother")

class Child(Mother, Father):
    pass

child = Child()
child.display()