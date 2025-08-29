 # ------------------------------
# Assignment 1: Design Your Own Class
# ------------------------------

# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery_percent += amount
        if self.battery_percent > 100:
            self.battery_percent = 100
        print(f"Battery charged to {self.battery_percent}%")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_gb}GB, Battery: {self.battery_percent}%")


# Derived Class: GamingSmartphone (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_percent=100, cooling_system=True):
        super().__init__(brand, model, storage_gb, battery_percent)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model}...")
        self.battery_percent -= 10
        print(f"Battery now at {self.battery_percent}%")

# Demo objects
print("=== Smartphone Demo ===")
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 512)

phone1.info()
phone1.make_call("123-456-7890")
phone1.charge(20)

phone2.info()
phone2.play_game("Call of Duty")
phone2.make_call("987-654-3210")
print("\n")


# ------------------------------
# Activity 2: Polymorphism Challenge
# ------------------------------

# Base Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")

# Derived Classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road")  # Safe for Windows terminals

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")   # Safe for Windows terminals

# Demo polymorphism
print("=== Polymorphism Demo ===")
vehicles = [Car(), Plane()]

for v in vehicles:
    v.move()
