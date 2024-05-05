# from config import password, add  # точечный импорт

# print(password)

# add(2, 8)

# from config import * # Из модуля импортируем все содержимое


# print(password)

# add(2, 8)


# import config # импорт модуля


# print(config.password)

# config.add(7, 8)


# from secret.calc import mult



""" Декомпозиция - разделение кода по модулям """


" Кастомные модули: lesson_6.py , calc.py "

" Встроенные (вложенные) можули: random.py , math , time , datetime "

# import random

# a = random.randint(1, 10)
# print(a)

# words = ["car", "house", "mouse", "1", 3, 5.6]
# print(random.choice(words))

# import time

# print("1")
# time.sleep(2)
# print("2")

# while True:
#     print("Loading...")
#     time.sleep(1)


# " Внешние модули "

from termcolor import cprint

cprint("Attention!", "red", attrs=["bold"])

cprint("Hello World!", "yellow", on_color="on_blue", attrs=["bold"])

