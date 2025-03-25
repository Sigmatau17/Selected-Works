import numpy as np
import matplotlib.pyplot as plt

def system(y, t, l, c_0, w_c, r): # Система дифференциальных уравнений
    return np.array([y[1], -1 * r * y[1]/l -1 * y[0]/(l * c_0 * np.cos(w_c * t))]) 

def rungekutta4(f, y0, t, args=()): # Метод Рунге-Кутты 4 порядка
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        k1 = f(y[i], t[i], *args)
        k2 = f(y[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(y[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(y[i] + k3 * h, t[i] + h, *args)
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y

l = 0.1 # Индуктивность катушки
r = 0.2 # Сопротивление
c_0 = 0.0003 # Начальная емкость
w_c = 1.25 * np.pi # Частота колебаний емкости

y0 = np.array([1, 1])
t = np.linspace(0, 0.39, 1000)
sol = rungekutta4(system, y0, t, args=(l, c_0, w_c, r))

plt.plot(t, sol[:, 0], 'b', label=r'q(t)') # График заряда
plt.legend(loc='best')
plt.ylabel('q(t)')
plt.xlabel('t')
plt.grid()
plt.show()

plt.plot(t, sol[:, 1], 'g', label=r'I(t)') # График силы тока
plt.legend(loc='best')
plt.ylabel('I(t)')
plt.xlabel('t')
plt.grid()
plt.show()

plt.plot(t, sol[:, 1], 'g', label=r'I(t)') # График силы тока и заряда вместе
plt.plot(t, sol[:, 0], 'b', label=r'q(t)') 
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()