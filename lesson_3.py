"Инкапсуляция"

class Laptops:
    def __init__(self, model, os, memory):
        self.model = model # Публичный
        self._os = os # Защищенный 
        self.__memory = memory # Приватный 

    "@ - декоратор"
    @property
    def memory(self):
        return self.__memory

    def info(self): # Публичный
        print(f"model - {self.model}, {self._os}")
        self._desktop()

    def _desktop(self): # Защищенный 
        print("Рабочий стол")

    def __password(self): # Приватный 
        print("password = 1234") 

    @property
    def password(self):
        return self.__password

huawei = Laptops("Huawei", "Windows 11", 512)

print(huawei.model)
print(huawei._os)
print(huawei.memory)
huawei.info()
# huawei._desktop()
huawei.password()


# import time

# def users(func):
#     def start():
#         print("Hello World!")
#         time.sleep(0.5)
#         print("1")
#         time.sleep(1)
#         print("2")
#         time.sleep(1)
#         print("3")
#         time.sleep(1)
#         print("start func")
#         time.sleep(1)
#         func()
#         print("Bye!")
#     return start






# @users
# def say():
#     print("Hi!")
# say()


"Множественное наследование"
class People: # Абстрактный класс и Родительский класс
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Father(People):
    def __init__(self, name, age, beard):
        People.__init__(self, name, age)
        self.beard = beard

    def work(self):
        print("Работа")

class Mother(People):
    def __init__(self, name, age, manikur):
        People.__init__(self, name, age)
        self.manikur = manikur

    def cook(self):
        print("Готовка")

class Child(Father, Mother):
    def __init__(self, name, age, beard, manikur, toys):
        Father.__init__(self, name, age, beard)
        Mother.__init__(self, name, age, manikur)
        self.toys = toys
        
    def cook(self):
        print("Я не умею готовить")

david = Child("David", 15, "Черная борода", "Розовый маникюр", "Много игрушек")
david.work()
david.cook()

