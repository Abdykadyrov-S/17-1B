"double underscore - dunder методы"
"Магические методы"

from typing import Any


class ElectroCar:
    def __init__(self, power, battery):
        self.power = power
        self.battery = battery

    def info(self, value):
        print(f"Мощность - {self.power} Vat \nЗаряд баттареи - {self.battery} Mah - {value}")

    def add(self, a , b):
        print(a + b)

    def __str__(self): # str == print
        return f"Мощность - {self.power} Vat \nЗаряд баттареи - {self.battery} Mah - это метод str"
    
    def __repr__(self): # repr == print
        return f"Мощность - {self.power} Vat \nЗаряд баттареи - {self.battery} Mah это метод repr"

    def __call__(self, a, b):
        print(a + b)

    "Магичиские методы для арифметических действий"

    def __add__(self, other): # +
        new_power = self.power + other.power
        return ElectroCar(new_power, self.battery)
    
    def __sub__(self, other): # -
        new_power = self.power - other.power
        return ElectroCar(new_power, self.battery)
    
    def __mul__(self, other): # *
        new_power = self.power * other.power
        return ElectroCar(new_power, self.battery)
    
    def __truediv__(self, other): # /
        new_power = self.power / other.power
        return ElectroCar(new_power, self.battery)
    
    def __floordiv__(self, other): # //
        new_power = self.power // other.power
        return ElectroCar(new_power, self.battery)
    
    "Магичиские методы для операторов сравнения"

    def __gt__(self, other): # >
        return self.battery > other.battery
    
    def __lt__(self, other): # <
        return self.battery < other.battery
    
    def __eq__(self, other): # ==
        return self.battery == other.battery
    
    def __ne__(self, other): # !=
        return self.battery != other.battery
    
    def __ge__(self, other): # >=
        return self.battery >= other.battery
    
    def __le__(self, other): # <=
        return self.battery <= other.battery

car = ElectroCar(120, 20000)
car_2 = ElectroCar(120, 20000)


# car.info(12)
# car.add(1, 2)
print(car) 
print("Helloo world!")
car(2 ,3)

"Магичиские методы для арифметических действий"
# print(car + car_2)
# print(car - car_2)
# print(car * car_2)
# print(car / car_2)
# print(car // car_2)

"Магичиские методы для операторов сравнения"

print(car > car_2)
print(car < car_2)
print(car == car_2)
print(car != car_2)
print(car >= car_2)
print(car <= car_2)
