class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        print(f'Color was changed to {new_color} from {self.color}')
        self.color = new_color


class Plane(Transport):  # DRY
    def __init__(self, model, year, color):
        super().__init__(model, year, color)


class Car(Transport):
    # class attribute
    counter = 0

    # constructor               # parameters
    def __init__(self, model, year, color='silver', penalties=0):
        # constructor matching
        super().__init__(model, year, color)
        # fields / attributes
        self.penalties = penalties
        Car.counter += 1

    # methods
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}.')


class Truck(Car):
    def __init__(self, model, year, color, penalties=0, load_capacity=0):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}!')
        else:
            print(f'You loaded products of type {product_type} ({weight} kg)!')


print('Start of program')
print(f'Factory CAR produced: {Car.counter}')

number = 7
bmw_car = Car('BMW X7', 2020, 'red')
print(number)
print(bmw_car)

print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'blue'
bmw_car.change_color('blue')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

honda_car = Car('HONDA Civic', 2000, 'yellow', 900)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

nissan_car = Car(year=2009, penalties=500, color='black', model='Nissan Patrol')
print(f'MODEL: {nissan_car.model} YEAR: {nissan_car.year} COLOR: {nissan_car.color} '
      f'PENALTIES: {nissan_car.penalties}')

bmw_car.drive('Osh')
nissan_car.drive('Kant')
nissan_car.drive('Tokmok')

boeing_plane = Plane('Boeing 727', 2023, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

volvo_truck = Truck('Volvo 300', 2021,
                    'yellow', 1200, 40000)
print(f'MODEL: {volvo_truck.model} YEAR: {volvo_truck.year} COLOR: {volvo_truck.color} '
      f'PENALTIES: {volvo_truck.penalties} LOAD CAPACITY: {volvo_truck.load_capacity} kg')

kia_k5 = Car('Kia K5', 2020)
print(f'MODEL: {kia_k5.model} YEAR: {kia_k5.year} COLOR: {kia_k5.color} '
      f'PENALTIES: {kia_k5.penalties}')

bmw_car.counter = 9

print(f'Factory CAR produced: {Car.counter}')
print('End of program')
