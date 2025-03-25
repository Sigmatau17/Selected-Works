import numpy as np

file = open("numbers", "r")
vyborka = []
print("Ведите параметр а")
a = float(input())
print("Ведите параметр сигма квадрат")
d = float(input())
print("Введи объем выборки")
n = int(input())
for i in range(n):
    number = float(file.readline())
    vyborka.append(number)
sum = 0
for i in range(len(vyborka)):
    sum = sum + vyborka[i]
mo = sum/n
print("оценка на параметр а = " + str(mo))
print("погрешность = " + str(np.abs(mo-a)))
disp = 0
for i in range(len(vyborka)):
    disp = disp + np.power(vyborka[i] - mo, 2)/n
print("оценка на дисперсию = " + str(disp))
print("погрешность = " + str(np.abs(disp-d)))