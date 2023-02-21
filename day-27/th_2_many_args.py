def add(*args):
    # *args -> It's a tuple
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    # **kwargs -> It's a dictionary
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

my_car_2 = Car(make="Tesla")
print(my_car_2.make)
print(my_car_2.model)
