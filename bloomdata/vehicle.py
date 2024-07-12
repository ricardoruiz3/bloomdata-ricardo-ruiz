'''
This file holds 2 classes: Vehicle and Convertible.
They are a child and parent class.
Imagine I want to list these vehivles on Craigslist
"Parent" class is the more generic class of the two
'''


class Vehicle():
    '''
    This is the class docstring.
    '''
    def __init__(self, make, model, color, year, mileage) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        '''
        This is the method docstring.
        '''
        return 'HOOOONK!'

    def drive(self, miles_driven):
        '''
        This is the method docstring.
        '''
        self.mileage += miles_driven
        return self.mileage

    def __repr__(self) -> str:
        return f'''A {self.color} {self.year} {self.make} {self.model}
        with {self.mileage} miles.'''


'''Imagine I want to make a very specific kind of vehicle, a convertible
The more specific class is "child" class
Convertible inherits from Vehicle.'''


class Convertible(Vehicle):
    '''
    This is the class docstring.
    '''
    def __init__(self, make, model, color, year,
                 mileage, top_down=True) -> None:
        '''
        This is the method docstring.
        '''
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        '''
        This is the method docstring.
        '''
        if self.top_down:
            self.top_down = False
            return 'Top is now UP!'
        else:
            self.top_down = True
            return 'Top is now DOWN!'

    def __repr__(self) -> str:
        return f'''A {self.color} {self.year} {self.make} {self.model}
        convertible with {self.mileage} miles.'''


if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Corolla', 'Gray', 2017, 60000)
    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())
    print(my_vehicle.top_down)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
