# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # base class
    # constructor
    def __init__(self, movement, wheels, fuel):
        self.movement = movement
        self.wheels = wheels
        self.fuel = fuel

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


class FlightVehicle(Vehicle):
    def __init__(self, movement, wheels, fuel):
        super().__init__(movement, wheels, fuel)
        # Can also do Vehicle.__init__(self, movement, wheels, fuel)
        self.movement = "flight"
        self.wheels = 3
        self.fuel = "jet fuel"

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


class Starship(FlightVehicle):
    def __init__(self, movement, wheels, fuel, weapon):
        super().__init__(movement, wheels, fuel)
        self.weapon = "blaster"

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


class GroundVehicle(Vehicle):
    def __init__(self, movement, wheels, fuel, armored=False):
        super().__init__(movement, wheels, fuel)

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


class Car(GroundVehicle):
    def __init__(self, movement, wheels, fuel, armored=False):
        super().__init__(movement, wheels, fuel, armored)

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


class Motorcycle(GroundVehicle):
    def __init__(self, movement, wheels, fuel, armored=False):
        super().__init__(movement, wheels, fuel, armored)

    def __str__(self):
        print(f"{self.movement}, {self.wheels}, {self.fuel}")


# motorcycle1 = Motorcycle("ground", 2, "gasoline", armored=True)
# print(motorcycle1.movement)

