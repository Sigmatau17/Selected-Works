import matplotlib.pyplot as plt
import numpy as np

g = 0.76 * 10**12
b = 1.33 * 10**(-9)
j = 1.33 * 10**(-9)

def w(k, g, b, j, a):
    return np.sqrt((g * b + g * j * k**2) * (g * b + g * j * k**2 + (np.sin(np.pi/2 - a))**2))

x = np.linspace(0, 0.05, 100)

y = w(x, g, b, j, 0)
plt.plot(x, y, label=f'a={0}')

y = w(x, g, b, j, np.pi/6)
plt.plot(x, y, label=f'a= {chr(960)}/6')

y = w(x, g, b, j, np.pi/4)
plt.plot(x, y, label=f'a={chr(960)}/4')

y = w(x, g, b, j, np.pi/2)
plt.plot(x, y, label=f'a={chr(960)}/2')

plt.xlabel('k, рад/нм')
plt.ylabel('w(k), рад/с')
plt.legend()
plt.title('Графики дисперсионного соотношения w(k)')
plt.grid(True)
plt.show()