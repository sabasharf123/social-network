#blueprint for what a vehicle is
class Vehicle:

    #Defines the fields of an object of this class
    #Vehicle("Versa")
    def __init__(self, name):
        self.name = name
        self.wheels = 4
        self.ignition = False
        self.passengers = []

    def set_number_of_wheels(self, wheels):
        self.wheels = wheels

    def turn_ignition(self, key):
        self.ignition = key

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

def main():
    #put all the stuff I want to do with different
    #vehicles in here
    SuperCar = Vehicle("Tesla")
    SuperCar.set_number_of_wheels(4)
    SuperCar.add_passengers("Drake")

    SpaceCraft = Vehicle("Apollo 13")
    SpaceCraft.add_passengers("Tom Hanks")

    print("Passengers in super car: " + str(SuperCar.passengers))
    print("Passengers in space craft: " + str(SpaceCraft.passengers))

main()
