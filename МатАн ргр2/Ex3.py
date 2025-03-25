import random
def f(x, y):
    return x**2 - y**2
print("Выберите способ выбора точек в узлах сетки: 1 - случайная точка узла; 2 - центр узла; 3 - максимумы x и y; 4 - минимумы x и y; 5 - минимум x, максимум y; 6 - максимум x, минимум y")
w = int(input())
print("Введите параметры a и b:")
a = float(input())
b = float(input())
print("Введите число n - количество отрезков разбиения отрезка [0, a]:")
n = int(input())
print("Введите число k - количество отрезков разбиения отрезка [0, b]:")
k = int(input())
Dx = a/n
Dy = b/k
Sq = Dx * Dy
X = []
if w == 1:
    for i in range(0, n):
        x = random.uniform(a*i/n, a*(i+1)/n)
        X.append(x)
    Y = []
    for j in range(0, k):
        y = random.uniform(b*j/k, b*(j+1)/k)
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
elif w == 2:
    for i in range(0, n):
        x = a*i/n + a/(2*n)
        X.append(x)
    Y = []
    for j in range(0, k):
        y = b*j/k + b/(2*k)
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
elif w == 3:
    for i in range(0, n):
        x = a*(i+1)/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = b*(j+1)/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
elif w == 4:
    for i in range(0, n):
        x = a*i/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = b*j/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
elif w == 5:
    for i in range(0, n):
        x = a*i/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = b*(j+1)/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
elif w == 6:
    for i in range(0, n):
        x = a*(i+1)/n
        X.append(x)
    Y = []
    for j in range(0, k):
        y = b*j/k
        Y.append(y)
    Sum = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            Sum = Sum + f(X[i], Y[j]) * Sq
else:
    print("Неправильный параметр...")
print("Интегральная сумма равна " + str(Sum) + ". При увеличении числа отрезков разбиения увеличивается точность интегральной суммы. В пределе она равна интегралу.")