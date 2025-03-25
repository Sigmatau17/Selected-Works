# Вариант 5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x1, x2 =  np.array([0, 1]), np.array([1, 0])
v1, v2 = np.array([-1, 2]), np.array([0, 0])
m1, m2 = 8, 7.2
F_ext = np.array([-3, 20])
h1, h2 = 0.15, 0.015
# k = 0 - для пункта 1, когда между телами нет сил приятжения, k = -30 - для пункта 2 и 3, где между телами есть сила притяжения.
# p = 0 - для пунктов 1 и 2, когда тела не теряют свою массу с тчением времени, p = 1 - для пункта 3, когда тело 2 теряет свою массу со временем.
t0, t_end = 0, 10

def Euler(v, x1, x2, F_ext, m0, k, p, h):
    def F_12_func(x1, x2, k):
        return np.array(k/((np.dot(x1 - x2, x1 - x2))**3) * (x1-x2)) # Сила притяжения тела 1 к телу 2, если поменять x1 и x2 в аргументе местами, то будет противоположная сила (антисимметричная билинейная форма)

    def a_func(F_ext, F_12, m):
        return (F_ext + F_12)/m # Суммарное ускорение данного тела
    
    X = [x1[0]]
    Y = [x1[1]]
    for t in np.arange(0, 10 + h, h):
        m = m0 * (0.92) ** (p * t)
        F_12 = F_12_func(x1, x2, k)
        a = a_func(F_ext, F_12, m)
        v = v + h * a
        x1 = x1 + h * v
        X.append(x1[0]), Y.append(x1[1])
    return X, Y


X1_h2, Y1_h2 = Euler(v1, x1, x2, F_ext, m1, -30, 0, h2) # Решение методом Эйлера для тела 1 при h = h2
X2_h2, Y2_h2 = Euler(v2, x2, x1, F_ext, m2, -30, 1, h2) # Решение методом Эйлера для тела 2 при h = h2

fig, ax = plt.subplots()
line1, = ax.plot([], [], 'r--', lw=2)  # Пунктирная линия для первой траектории
line2, = ax.plot([], [], 'g--', lw=2)  # Пунктирная линия для второй траектории
point1, = ax.plot([], [], 'bo', markersize=5, label='Тело 1')  # Первая точка (синий круг)
point2, = ax.plot([], [], 'mo', markersize=5, label='Тело 2')  # Вторая точка (пурпурный круг)

# Устанавливаем границы графика
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.legend()

# Функция для инициализации анимации
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    return line1, line2, point1, point2

# Функция для обновления анимации
def update(frame):
    line1.set_data(X1_h2[:frame], Y1_h2[:frame])  # Обновляем траекторию
    line2.set_data(X2_h2[:frame], Y2_h2[:frame])
    point1.set_data(X1_h2[frame], Y1_h2[frame])  # Обновляем положение точки
    point2.set_data(X2_h2[frame], Y2_h2[frame])
    return line1, line2, point1, point2

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=len(X2_h2), init_func=init, blit=True, interval=100)

# Отображаем анимацию
plt.show()