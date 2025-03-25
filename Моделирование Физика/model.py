import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Параметры системы
N = 500  # количество частиц
L = 46.42  # длина стороны куба в нм
T = 300.0  # температура в К
k_B = 1.38e-23  # постоянная Больцмана
mass = 1e-28  # масса

# Инициализация частиц
positions = np.random.rand(N, 3) * L  # случайные позиции в кубе
velocities = np.random.normal(0, np.sqrt((3 * k_B * T )/ mass), (N, 3))  # скорости частиц

# Потенциальная энергия взаимодействия
def potential_energy(r):
    a = -1 * 10**(-20) 
    b = 10 ** (-21)
    return b / (r)**5 + a / (r)**3

# Основной цикл моделирования
time_steps = 10
dt = 0.01  # шаг по времени

# Сохранение траекторий для анимации и энергии
trajectories = []
energies = []

for step in range(time_steps):
    # Обновление позиций
    positions += velocities * dt
    
    # Обработка границ (периодические условия)
    positions %= L
    
    # Расчет сил и обновление скоростей
    forces = np.zeros_like(positions)
    
    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[j] - positions[i]
            r_vec -= L * np.round(r_vec / L)  # периодические границы
            r = np.linalg.norm(r_vec)
            if r > 0 and r < 1:  # избегаем деления на ноль
                f = potential_energy(r) / r * r_vec
                forces[i] += f
                forces[j] -= f

    velocities += forces * dt / mass  # делим на массу

    # Сохраняем позиции для анимации
    trajectories.append(np.copy(positions))

    # Расчет средней кинетической энергии
    kinetic_energy = 0.5 * mass * np.sum(velocities**2)
    average_energy = kinetic_energy / N
    energies.append(average_energy)

# Увеличили объем сосуда в 2 раза в нм
L = 58.48  
for step in range(time_steps):
    # Обновление позиций
    positions += velocities * dt
    
    # Обработка границ (периодические условия)
    positions %= L
    
    # Расчет сил и обновление скоростей
    forces = np.zeros_like(positions)
    
    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[j] - positions[i]
            r_vec -= L * np.round(r_vec / L)  # периодические границы
            r = np.linalg.norm(r_vec)
            if r > 0 and r < 1:  # избегаем деления на ноль
                f = potential_energy(r) / r * r_vec
                forces[i] += f
                forces[j] -= f

    velocities += forces * dt / mass  # делим на массу (предполагаем массу = 1)

    # Сохраняем позиции для анимации
    trajectories.append(np.copy(positions))

    # Расчет средней кинетической энергии
    kinetic_energy = 0.5 * mass * np.sum(velocities**2)
    average_energy = kinetic_energy / N
    energies.append(average_energy)

# Визуализация с помощью анимации
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scat = ax.scatter([], [], [], s=2)

ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)
ax.set_title('Движение частиц газа')

# Функция для обновления кадров анимации
def update(frame):
    scat._offsets3d = (trajectories[frame][:, 0], trajectories[frame][:, 1], trajectories[frame][:, 2])
    return scat,

# Создание анимации
ani = FuncAnimation(fig, update, frames=len(trajectories), interval=50)

plt.show()

# Визуализация средней энергии газа во времени
plt.figure()
plt.plot(energies, marker='o', linestyle='-', color='b')
plt.title('Средняя кинетическая энергия газа')
plt.xlabel('Шаг времени')
plt.ylabel('Средняя энергия (Дж)')
plt.grid()
plt.show()
print(energies)

# Визуализация температуры газа во времени
temperatures = []
for i in range(len(energies)):
    temperatures.append(energies[i]/(1.5 * k_B))

plt.figure()
plt.plot(temperatures, marker='o', linestyle='-', color='b')
plt.title('Температура газа')
plt.xlabel('Шаг времени')
plt.ylabel('Температура газа (К)')
plt.grid()
plt.show()