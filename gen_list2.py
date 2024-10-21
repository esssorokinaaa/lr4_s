import random

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(3, 9))
print(rand_list)

#Используя random.randint(), мы можем добавлять случайные числа в список.

# Python3 code to demonstrate
# to generate random number list
# using random.sample()
import random

# using random.sample()
# to generate random number list
res = random.sample(range(1, 50), 7)

# printing result
print("Random number list is : " + str(res))

#random.sample - единственная функция полезности выполняет именно то, что требуется в условии задачи: она генерирует N случайных чисел в списке в указанном диапазоне и возвращает требуемый список.


# Python3 code to demonstrate
# to generate random number list
# using list comprehension + randrange()
import random

# using list comprehension + randrange()
# to generate random number list
res = [random.randrange(1, 50, 1) for i in range(7)]

# printing result
print("Random number list is : " + str(res))

#Функция randrange используется для выполнения задачи генерации случайных чисел.

# Method 3: For Loop Random Int List [0, 51]
import random
lis = []
for _ in range(10):
    lis.append(random.randint(0, 51))
print(lis)

# importing numpy module
import numpy as np

# print the list of 10 integers from 3  to 7
print(list(np.random.randint(low=3, high=8, size=10)))

# print the list of 5 integers from 0 to 2
# if high parameter is not passed during
# function call then results are from [0, low)
print(list(np.random.randint(low=3, size=5)))

# функция возвращает случайные целые числа из «дискретно-равномерного» распределения целочисленного типа данных

import numpy as np

# generates list of 4 float values
print(np.random.random_sample(size=4))

# generates 2d list of 4*4
print(np.random.random_sample(size=(4, 4)))

#функция возвращает случайные значения с плавающей точкой в полуоткрытом интервале [0,0, 1,0)

#Реализация каждого способа получения случайного числа в виде отдельной функции

#1
def my_rand1():
    return random.randint(3, 9) #Функция `random.randint()` принимает два аргумента: нижнюю границу и верхнюю границу.
#2
def my_rand2():
    return random.sample(range(1, 50), 7) #Функция `random.sample()` выбирает случайные элементы из заданного списка.

#3
def my_rand3():
    return [random.randrange(1, 50, 1) for i in range(7)] #Функция `random.randrange()` позволяет генерировать случайные числа внутри указанного диапазона.

#4
def my_rand4():
    lis = []
    for _ in range(10):
        lis.append(random.randint(0, 51))
    return lis #Цикл генерирует список случайных чисел от 0 до 51.

#5
def my_rand5():
    return list(np.random.randint(low=3, high=8, size=10))

def my_rand6():
    return list(np.random.randint(low=3, size=5))
#Использование модуля `numpy` для генерации случайных чисел.

#6
def my_rand7():
    return np.random.random_sample(size=4)

def my_rand8():
    return np.random.random_sample(size=(4, 4))
#Генерация списка случайных вещественных чисел от 0 до 1.