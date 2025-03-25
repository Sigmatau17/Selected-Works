import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time

#Функция и её градиент
def f(x, y):
    return (2*x**2 + y**2) * np.exp(-x**2 - y**2)
def grad(x, y):
    return (np.exp(-x**2 - y**2) * (-4*x**3 + 4*x - 2*x*y**2), np.exp(-x**2 - y**2) * (-2*y**3 - 4*x**2*y + 2*y))

#Векторное поле градиента
x,y = np.meshgrid(np.linspace(-2,2,25),np.linspace(-2,2,25))
devx = grad(x, y)[0]
devy = grad(x, y)[1]
plt.streamplot(x,y,devx,devy, density=1)
plt.title('Gradient Vector Field')
plt.grid()
plt.show()

#Линии уровня
x,y = np.meshgrid(np.arange(-2,2,0.01),np.arange(-2,2,0.01))
z = (2*x**2 + y**2) * np.exp(-x**2 - y**2)
fig, ax = plt.subplots()
CS = ax.contour(x,y,z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Level lines')
plt.grid()
plt.show()

#Градиентный спуск
x = 0.5
y = 0.5
fP = f(x, y)
df = 1
a = 0.01
i = 0
X = []
Y = []
Z = []
start_time = time.time()
while np.abs(df) > 0.00000001:
    x = x - a * grad(x, y)[0]
    y = y - a * grad(x, y)[1]
    gradP = grad(x, y)
    df = f(x, y) - fP
    fP = f(x, y)
    i = i + 1
    X.append(x)
    Y.append(y)
    Z.append(fP)
end_time = time.time()
elapsed_time = end_time - start_time

#Результаты
print('Время нахождения минимума: ', elapsed_time)
print('Точка минимума функции: (' + str(x) + ',' + str(y) + ')')
print('Значение функции в точке: ' + str(fP))
print('Значение градиента функции в точке: ' + str(grad(x, y)))
print('Количество шагов: ' + str(i))

#3D График с треком
plt.style.use('_mpl-gallery')
x,y = np.meshgrid(np.linspace(-2,2,25),np.linspace(-2,2,))
z = (2*x**2 + y**2) * np.exp(-x**2 - y**2)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, z, cmap=cm.Blues)
plt.title('3D Plot + point track')
plt.plot(X, Y, Z, color = 'g')
plt.grid()
plt.show()
