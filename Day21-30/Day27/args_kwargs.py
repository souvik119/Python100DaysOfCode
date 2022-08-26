# unlimited positional arguments

# def add(*args):
#     #args is a tuple
#     sum = 0
#     for n in args:
#         sum += n
#     return sum


# print(add(1, 2, 3, 5))


# unlimited keyword arguments

# def calculator(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculator(2, add=3, multiply=5)


# can use .get() method instead of [] in dictionary, benefit being if no value is found None is assigned instead of key error
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model) # since we used .get(), this is going to print None instead of failing for key error