import numpy as np
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.arange(-10,10,0.01),np.arange(-10,10,0.01))
z = np.abs(x) + np.abs(y) - np.abs(x+y)
fig, ax = plt.subplots()
CS = ax.contour(x,y,z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxy projection')
plt.grid()
plt.show()

x,y = np.meshgrid(np.arange(-10,10,0.01),np.arange(-10,10,0.01))
z = np.abs(x) + np.abs(y) - np.abs(x+y)
fig, ax = plt.subplots()
CS = ax.contour(y,z,x)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oyz projection')
plt.grid()
plt.show()

x,y = np.meshgrid(np.arange(-10,10,0.01),np.arange(-10,10,0.01))
z = np.abs(x) + np.abs(y) - np.abs(x+y)
fig, ax = plt.subplots()
CS = ax.contour(x,z,y)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxz projection')
plt.grid()
plt.show()