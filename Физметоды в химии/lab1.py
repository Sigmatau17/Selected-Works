# Вариант 5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x1, x2 =  np.array([0, 1]), np.array([1, 0])
v1, v2 = np.array([-1, 2]), np.array([0, 0])
m1, m2 = 8, 7.2
F_ext = np.array([-3, 20])
h1, h2 = 0.15, 0.015

# Функция анимации дивжения тел для пунктов 2 и 3.
def Animation(X1, Y1, X2, Y2, h, Method, speed):
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], 'r--', lw=2)
    line2, = ax.plot([], [], 'g--', lw=2)
    point1, = ax.plot([], [], 'bo', markersize=5, label='Тело 1')
    point2, = ax.plot([], [], 'mo', markersize=5, label='Тело 2')
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Траектории движения тел при h = ' + str(h) + ', полученные методом ' + Method)

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        point1.set_data([], [])
        point2.set_data([], [])
        return line1, line2, point1, point2
    
    def update(frame):
        line1.set_data(X1[:frame], Y1[:frame])
        line2.set_data(X2[:frame], Y2[:frame])
        point1.set_data(X1[frame], Y1[frame])
        point2.set_data(X2[frame], Y2[frame])
        return line1, line2, point1, point2

    ani = FuncAnimation(fig, update, frames=len(X2), init_func=init, blit=True, interval=speed)
    plt.show()

# Функция построения графиков для пункта 1.
def Plot(X1_h1, Y1_h1, X1_h2, Y1_h2, Method):
    plt.scatter(X1_h1, Y1_h1, s=5, color='blue', label='Траектория тела 1 при h = ' + str(h1) + ', полученные методом ' + Method)
    plt.scatter(X1_h2, Y1_h2, s=5, color='green', label='Траектория тела 1 при h = ' + str(h2) + ', полученные методом ' + Method)
    plt.title('Траектории тела 1 при разных h')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-50, 50)
    plt.ylim(-25, 200)
    plt.grid(True)
    plt.legend()
    plt.show()

# Метод Эйлера.
def Euler(v1, v2, x1, x2, m1_0, m2_0, F_ext, k, p, q, h):
    def F_12_func(x1, x2, k):
        return np.array(k/((np.dot(x1 - x2, x1 - x2))**3) * (x1-x2)) # Сила притяжения тела 1 к телу 2, если поменять x1 и x2 в аргументе местами, то будет противоположная сила (антисимметричная билинейная форма)

    def a_func(F_ext, F_12, m):
        return (F_ext + F_12)/m # Суммарное ускорение данного тела.
    
    X1, Y1 = [x1[0]], [x1[1]]
    X2, Y2 = [x2[0]], [x2[1]]

    for t in np.arange(0, 10 + h, h):
        m1 = m1_0 * (1 - p/100) ** t # Тело 1 теряет p% своей массы за единицу времени.
        m2 = m2_0 * (1 - q/100) ** t # Тело 2 теряет q% своей массы за единицу времени.
        a1 = a_func(F_ext, F_12_func(x1, x2, k), m1)
        a2 = a_func(F_ext, F_12_func(x2, x1, k), m2)

        v1 = v1 + h * a1
        x1 = x1 + h * v1
        X1.append(x1[0]), Y1.append(x1[1])
        
        v2 = v2 + h * a2
        x2 = x2 + h * v2
        X2.append(x2[0]), Y2.append(x2[1])

    return X1, Y1, X2, Y2

def Heun(v1, v2, x1, x2, m1_0, m2_0, F_ext, k, p, q, h):
    def F_12_func(x1, x2, k):
        return np.array(k/((np.dot(x1 - x2, x1 - x2))**3) * (x1-x2)) # Сила притяжения тела 1 к телу 2, если поменять x1 и x2 в аргументе местами, то будет противоположная сила (антисимметричная билинейная форма)

    def a_func(F_ext, F_12, m):
        return (F_ext + F_12)/m # Суммарное ускорение данного тела.
    
    X1, Y1 = [x1[0]], [x1[1]]
    X2, Y2 = [x2[0]], [x2[1]]

    for t in np.arange(0, 10 + h, h):
        m1 = m1_0 * (1 - p/100) ** t # Тело 1 теряет p% своей массы за единицу времени.
        m2 = m2_0 * (1 - q/100) ** t # Тело 2 теряет q% своей массы за единицу времени.
        a1 = a_func(F_ext, F_12_func(x1, x2, k), m1)
        a2 = a_func(F_ext, F_12_func(x2, x1, k), m2)

        v1_pred = v1 + h * a1
        x1_pred = x1 + h * v1_pred
        v2_pred = v2 + h * a2
        x2_pred = x2 + h * v2_pred

        a1_pred = a_func(F_ext, F_12_func(x1_pred, x2_pred, k), m1)
        a2_pred = a_func(F_ext, F_12_func(x2_pred, x1_pred, k), m2)

        v1 = v1 + h/2 * (a1 + a1_pred)
        x1 = x1 + h/2 * (v1 + v1_pred)
        v2 = v2 + h/2 * (a2 + a2_pred)
        x2 = x2 + h/2 * (v2 + v2_pred)

        X1.append(x1[0]), Y1.append(x1[1])
        X2.append(x2[0]), Y2.append(x2[1])

    return X1, Y1, X2, Y2  

def Verlet(v1, v2, x1, x2, m1_0, m2_0, F_ext, k, p, q, h):
    def F_12_func(x1, x2, k):
        return np.array(k/((np.dot(x1 - x2, x1 - x2))**3) * (x1-x2)) # Сила притяжения тела 1 к телу 2, если поменять x1 и x2 в аргументе местами, то будет противоположная сила (антисимметричная билинейная форма)

    def a_func(F_ext, F_12, m):
        return (F_ext + F_12)/m # Суммарное ускорение данного тела.
    
    X1, Y1 = [x1[0]], [x1[1]]
    X2, Y2 = [x2[0]], [x2[1]]

    for t in np.arange(0, 10 + h, h):
        m1 = m1_0 * (1 - p/100) ** t # Тело 1 теряет p% своей массы за единицу времени.
        m2 = m2_0 * (1 - q/100) ** t # Тело 2 теряет q% своей массы за единицу времени.
        a1 = a_func(F_ext, F_12_func(x1, x2, k), m1)
        a2 = a_func(F_ext, F_12_func(x2, x1, k), m2)

        x_1_halfstep = x1 + 0.5 * v1 * h
        v1 = v1 + h * a1
        x1 = x_1_halfstep + 0.5 * v1 * h
        X1.append(x1[0]), Y1.append(x1[1])
        
        x_2_halfstep = x2 + 0.5 * v2 * h
        v2 = v2 + h * a2
        x2 = x_2_halfstep + 0.5 * v2 * h
        X2.append(x2[0]), Y2.append(x2[1])

    return X1, Y1, X2, Y2  

# Пункт 1
"""t = np.linspace(0, 10, 100)
X1_real, Y1_real = -0.1875 * t ** 2 - t, 1.25 * t ** 2 + 2 * t + 1 # Аналитическое решение
plt.plot(X1_real, Y1_real, label='Аналитическое решение', color = 'black')
X1_h1, Y1_h1, X2_h1, Y2_h1 = Euler(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h1) # Решение методом Эйлера для тела 1 при h = h1
X1_h2, Y1_h2, X2_h2, Y2_h2 = Euler(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h2) # Решение методом Эйлера для тела 1 при h = h2
Plot(X1_h1, Y1_h1, X1_h2, Y1_h2, "Euler")

X1_h1, Y1_h1, X2_h1, Y2_h1 = Heun(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h1) # Решение методом Хойна для тела 1 при h = h1
X1_h2, Y1_h2, X2_h2, Y2_h2 = Heun(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h2) # Решение методом Хойна для тела 1 при h = h2
Plot(X1_h1, Y1_h1, X1_h2, Y1_h2, "Heun")

X1_h1, Y1_h1, X2_h1, Y2_h1 = Verlet(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h1) # Решение методом Верле для тела 1 при h = h1
X1_h2, Y1_h2, X2_h2, Y2_h2 = Verlet(v1, np.array([0, 0]), x1, np.array([0, 0]), m1, m2, F_ext, 0, 0, 0, h2) # Решение методом Верле для тела 1 при h = h2
Plot(X1_h1, Y1_h1, X1_h2, Y1_h2, "Verlet")

# Пункт 2
X1, Y1, X2, Y2 = Euler(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h1) # Решение методом Эйлера при h = h1
Animation(X1, Y1, X2, Y2, h1, "Euler", 100)
X1, Y1, X2, Y2 = Euler(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h2) # Решение методом Эйлера при h = h2
Animation(X1, Y1, X2, Y2, h2, "Euler", 10)

X1, Y1, X2, Y2 = Heun(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h1) # Решение методом Хойна при h = h1
Animation(X1, Y1, X2, Y2, h1, "Heun", 100)
X1, Y1, X2, Y2 = Heun(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h2) # Решение методом Хойна при h = h2
Animation(X1, Y1, X2, Y2, h2, "Heun", 10)

X1, Y1, X2, Y2 = Verlet(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h1) # Решение методом Верле при h = h1
Animation(X1, Y1, X2, Y2, h1, "Verlet", 100)
X1, Y1, X2, Y2 = Verlet(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 0, h2) # Решение методом Верле при h = h2
Animation(X1, Y1, X2, Y2, h2, "Verlet", 10)"""

# Пункт 3
X1, Y1, X2, Y2 = Euler(v1, v2, x1, x2, m1, m2, F_ext, -100, 0, 8, h1) # Решение методом Эйлера при h = h1
Animation(X1, Y1, X2, Y2, h1, "Euler", 100)
X1, Y1, X2, Y2 = Euler(v1, v2, x1, x2, m1, m2, F_ext, -100, 0, 8, h2) # Решение методом Эйлера при h = h2
Animation(X1, Y1, X2, Y2, h2, "Euler", 10)

X1, Y1, X2, Y2 = Heun(v1, v2, x1, x2, m1, m2, F_ext, -100, 0, 8, h1) # Решение методом Хойна при h = h1
Animation(X1, Y1, X2, Y2, h1, "Heun", 100)
X1, Y1, X2, Y2 = Heun(v1, v2, x1, x2, m1, m2, F_ext, -100, 0, 8, h2) # Решение методом Хойна при h = h2
Animation(X1, Y1, X2, Y2, h2, "Heun", 10)

X1, Y1, X2, Y2 = Verlet(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 8, h1) # Решение методом Верле при h = h1
Animation(X1, Y1, X2, Y2, h1, "Verlet", 100)
X1, Y1, X2, Y2 = Verlet(v1, v2, x1, x2, m1, m2, F_ext, -30, 0, 8, h2) # Решение методом Верле при h = h2
Animation(X1, Y1, X2, Y2, h2, "Verlet", 10)