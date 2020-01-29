# Parent class
class Vehicle:
    # Initiator
    def __init__(self, model, color):
        self.model = model
        self.color = color

# Child class
class Car(Vehicle):
    def __init__(self, model, color):
        # Inheriting the initiator from parent class
        super().__init__(model, color)

    # Method
    def drive(self, miles):
        print("I just drove " + str(miles) + " miles!")

    # Necessary  to change the car's color because due to encapsulation...
    # ... color is treated as private attribute
    def getPaintJob(self, paintColor):
        self.color = paintColor

# Child class
class Bike(Vehicle):
    def __init__(self, model, color):
        # Inheriting the initiator from parent class
        super().__init__(model, color)

    # Method
    def drive(self, miles):
        print("I just drove " + str(miles) + " miles!")

    # Necessary  to change the car's color because due to encapsulation...
    # ... color is treated as private attribute
    def getPaintJob(self, paintColor):
        self.color = paintColor

# Polymorphism: applies common interface to multiple classes
def milesReward(automobile, miles):
    automobile.drive(miles)
    if (miles > 20):
        print(str(automobile.model) + " has received miles reward for travelling " + str(miles) + " miles!")



myLambo = Car("Urus", "blue")
myLambo.drive(25)
print("The " + str(myLambo.model) + " is " + str(myLambo.color) + "!")
print("Getting paint job...")

# Will not work because color is a private attribute
myLambo.color = "pink"

myLambo.getPaintJob("magenta")
print("The " + str(myLambo.model) + " is now " + str(myLambo.color) + "!")

myActiva = Bike("Activa 5G", "Yellow")

milesReward(myActiva, 28)
milesReward(myLambo, 40)
