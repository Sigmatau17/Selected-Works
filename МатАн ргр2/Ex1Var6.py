import numpy as np
import matplotlib.pyplot as plt

#Пункт 3. Векторные линии поля.
x,y = np.meshgrid(np.linspace(-2,2,25),np.linspace(-2,2,25))
devx = np.sin(x + y**2)
devy = 2 * y * np.sin(x + y**2)
plt.streamplot(x,y,devx,devy, density=1)
plt.title('Vector Lines')
plt.grid()
plt.show()

#Пункт 5. Линии уровня потенциала.
x,y = np.meshgrid(np.arange(-3,3,0.01),np.arange(-3,3,0.01))
u = -1 * np.cos(x + y**2)
fig, ax = plt.subplots()
CS = ax.contour(x,y,u)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxy projection')
plt.grid()
plt.show()

x,y = np.meshgrid(np.arange(-3,3,0.01),np.arange(-3,3,0.01))
u = -1 * np.cos(x + y**2)
fig, ax = plt.subplots()
CS = ax.contour(y,u,x)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oyz projection')
plt.grid()
plt.show()

x,y = np.meshgrid(np.arange(-3,3,0.01),np.arange(-3,3,0.01))
u = -1 * np.cos(x + y**2)
fig, ax = plt.subplots()
CS = ax.contour(x,u,y)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxz projection')
plt.grid()
plt.show()