import numpy as np
import random
def f(x, y):
    return x**2 - y**2
def phi(x):
    return np.cos(np.pi * x/2)
def fK(x, y):
    if x >= -2 and x <= 2 and y >= -1 and y <= phi(x):
        return x**2 - y**2
    else:
        return 0
print("Выберите способ выбора точек в узлах сетки: 1 - случайная точка узла; 2 - центр узла; 3 - максимумы x и y; 4 - минимумы x и y; 5 - минимум x, максимум y; 6 - максимум x, минимум y")
w = int(input())
print("Введите число n - количество отрезков разбиения вдоль оси Ox:")
n = int(input())
print("Введите число k - количество отрезков разбиения вдоль оси Oy:")
k = int(input())
Dx = 4/n
Dy = 2/k
Sq = Dx * Dy
X = []
if w == 1:
    for i in range(0, n):
        x = random.uniform(-2 + 4*i/n, -2 + 4*(i+1)/n)
        X.append(x)
    Y = []
    for j in range(0, k):
        y = random.uniform(-1 + 2*j/k, -1 + 2*(j+1)/k)
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
elif w == 2:
    for i in range(0, n):
        x = -2 + 4*i/n + 4/(2*n)
        X.append(x)
    Y = []
    for j in range(0, k):
        y = -1 + 2*j/k + 2/(2*k)
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
elif w == 3:
    for i in range(0, n):
        x = -2 + 4*(i+1)/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = -1 + 2*(j+1)/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
elif w == 4:
    for i in range(0, n):
        x = -2 + 4*i/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = -1 + 2*j/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
elif w == 5:
    for i in range(0, n):
        x = -2 + 4*i/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = -1 + 2*(j+1)/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
elif w == 6:
    for i in range(0, n):
        x = -2 + 4*(i+1)/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = -1 + 2*j/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + fK(X[i], Y[j]) * Sq
else:
    print("Неправильный параметр...")
print("Интегральная сумма равна " + str(Sum) + ". При увеличении числа отрезков разбиения увеличивается точность интегральной суммы. В пределе она равна интегралу.")