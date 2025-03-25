import math as mt
import numpy as np
import matplotlib.pyplot as plt

In = open('in.txt', 'r')
X = float(In.readline())
h = float(In.readline())
In.close()

def ydev(x, y):
    return (2*x - y + 1)/(x - 2*y + 1)

# Приближенное решение с шагом h:
xn = 0
yn = 4
xdots = []
ydots = []
xdots.append(xn)
ydots.append(yn)
def rungekutta(xn, yn, h):
    k1 = ydev(xn, yn)
    k2 = ydev(xn + h/2, yn + k1*h/2)
    k3 = ydev(xn + h/2, yn + k2*h/2)
    k4 = ydev(xn + h, yn + k3*h)
    return yn + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
while (xn < X):
    yn = rungekutta(xn, yn, h)
    xn = xn + h
    ydots.append(yn)
    xdots.append(xn)
plt.plot(xdots, ydots)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
xlen = len(xdots)
Out = open('out.txt', 'w+')
Out.write("Approximate solution with a step h" + '\n')
Out.write("x" + '\t' + "|" + '\t' + "y" + '\n')
Out.write("--------------------------" + '\n')
for i in range (xlen):
    Out.write(str(xdots[i]) + '\t' + "|" + '\t' + str(ydots[i]) + '\n')

# Приближенное решение с шагом h/10:
h = h/10
xn = 0
yn = 4
xdots2 = []
ydots2 = []
xdots2.append(xn)
ydots2.append(yn)
def rungekutta(xn, yn, h):
    k1 = ydev(xn, yn)
    k2 = ydev(xn + h/2, yn + k1*h/2)
    k3 = ydev(xn + h/2, yn + k2*h/2)
    k4 = ydev(xn + h, yn + k3*h)
    return yn + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
while (xn < X):
    yn = rungekutta(xn, yn, h)
    xn = round(xn + h, 4)
    ydots2.append(yn)
    xdots2.append(xn)
plt.plot(xdots2, ydots2)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
xlen = len(xdots2)
Out.write("Approximate solution with a step h/10" + '\n')
Out.write("x" + '\t' + "|" + '\t' + "y" + '\n')
Out.write("--------------------------" + '\n')
for i in range (xlen):
    Out.write(str(xdots2[i]) + '\t' + "|" + '\t' + str(ydots2[i]) + '\n')
Out.close()