"ООП - Объектно Ориентрованное Программирование"
"DRY - Don`t Repeat Yuorself == не повторяй себя"

SuperCar = 12

super_car = 34


class Car: # чертеж или же шаблон
    wheels = 4 # Атрибут/поле/свойства класса
    "self - сам объект" 
    "__init__ - конструктор"
    def __init__(self, model, color): 
        self.model = model # Атрибут/поле/свойства объекта
        self.color = color
        self.is_start = False

    def info(self): 
        print(f"Model - {self.model}, color - {self.color}")

    def start(self): 
        self.is_start = True
        print(f"Машина {self.model} завелась")

    def drive(self):
        if self.is_start == True:
            print(f"Машина {self.model} поехала")
        else:
            print(f"Машина {self.model} не заведена")

    def stop(self):
        self.is_start = False
        print(f"Машина {self.model} заглушена")

super_car = Car("Mersedes - cls", "black")
super_car_2 = Car("BMW - m5", "white")
# print(super_car.wheels)
# print(super_car.model)
# print(super_car_2.wheels)
# print(super_car_2.model)
super_car.info()
print(super_car.is_start)
super_car.drive()
print(super_car.is_start)
super_car.start()
print(super_car.is_start)
super_car.drive()
super_car.stop()
print(super_car.is_start)
super_car.drive()
super_car_2.info()

