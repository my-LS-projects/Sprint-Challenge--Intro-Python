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
    def __init__(self):
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()


class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()


class Car(GroundVehicle):
    def __init__(self):
        super().__init__()


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()


# motorcycle1 = Motorcycle("ground", 2, "gasoline", armored=True)
# print(motorcycle1.movement)

