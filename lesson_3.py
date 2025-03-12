class Person:
    def __init__(self, full_name, age):
        self.__full_name = full_name
        self.__age = age

    @property
    def full_name(self):
        return self.__full_name

    @property
    def age(self):
        return self.__age


class Car:
    def __init__(self, model, year, color, owner):
        self.__model = model
        self.__year = year
        self.__color = color
        if type(owner) is Person:
            self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return (f'MODEL: {self.__model}, YEAR: {self.__year}, COLOR: {self.__color}, '
                f'OWNER INFO: {self.__owner.full_name}')

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __le__(self, other):
        return self.year <= other.year


class FuelCar(Car):
    __total_fuel = 0

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.show_fuel_remain()

    @classmethod
    def show_fuel_remain(cls):
        print(f'Factory FUEL_CAR has: {cls.__total_fuel} litters fuel.')

    @staticmethod
    def show_fuel_standards():
        return 'AI 95'

    def __init__(self, model, year, color, fuel_bank, owner):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color, owner)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.')

    def __str__(self):
        return super().__str__() + f', FUEL_BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery, owner):
        Car.__init__(self, model, year, color, owner)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity.')

    def __str__(self):
        return super().__str__() + f', BATTERY: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery, owner):
        FuelCar.__init__(self, model, year, color, fuel_bank, owner)
        ElectricCar.__init__(self, model, year, color, battery, owner)

    # def drive(self):
    #     print(f'Car {self.model} is driving by fuel or electricity.')


# some_car = Car('Ford Mustang', 2020, 'black')
# print(some_car)


FuelCar.buy_fuel(500)

p1 = Person('Jim Brown', 55)

ford_car = FuelCar('Ford Mustang', 2020,
                   'black', 85, p1)
print(ford_car)

tesla_car = ElectricCar('Tesla Model X', 2022,
                        'red', 15000, p1)
print(tesla_car)

# p2 =  Person('Jane Stone', 26)
#  a = b

toyota_car = HybridCar('Toyota Prius', 2009, 'blue',
                       60, 10000,
                       Person('Jane Stone', 26))
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())

number_1, number_2 = 2, 5
print(f'Number one is greater than number two: {number_1 > number_2}')
print(f'Number one is less than number two: {number_1 < number_2}')
print(f'Ford car is less than Toyota car: {ford_car < toyota_car}')
print(f'Ford car is not same with Toyota car: {ford_car != toyota_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Sum of fuel banks: {ford_car + toyota_car}')

# FuelCar.total_fuel -= 100
FuelCar.show_fuel_remain()
print(f'By standard FUEL_CAR factory uses fuel of mark'
      f' {FuelCar.show_fuel_standards()}')
