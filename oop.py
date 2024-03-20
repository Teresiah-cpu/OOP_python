class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class Car(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} stops"

class Motorcycle(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} revs the engine and starts"

    def stop(self):
        return f"The {self.year} {self.make} {self.model} applies the brakes and stops"

# Creating instances of Car and Motorcycle
my_car = Car("Toyota", "Camry", 2020)
my_motorcycle = Motorcycle("Honda", "CBR500R", 2019)

# Using the start and stop methods without needing to know the internal implementation
print(my_car.start())




#In Python, __init__ is a special method used for initializing objects of a class. It's called automatically when a new instance of the class is created. Within the __init__ method, you can define the initial state of the object by assigning values to its attributes.

#self is a reference to the instance of the class itself. It's used to access variables and methods within the class. When you create a new instance of a class, Python automatically passes the instance itself as the first argument to every method defined within the class, including __init__. By convention, this argument is named self, but you can name it differently if you want. Using self, you can access and modify the attributes and methods of the instance within the class.
