import numpy as np
import matplotlib.pyplot as plt

wavelength_excitation = np.arange(250, 481, 3)  # Длины волн поглощения
wavelength_emission = np.arange(270, 603, 3)  # Длины волн эмиссии

to5 = np.loadtxt("to-5 в метаноле флуо.txt")
to5 = to5[:, 1:]

meoh = np.loadtxt("чистый метанол флуо.txt")
meoh = meoh[:, 1:]

sum = to5 - meoh
sum[sum < 0] = 0
max_index = np.unravel_index(np.argmax(sum, axis=None), sum.shape)
sum[max_index[0]][max_index[1]] = 25
#sum[29][2] = 10

# Построение 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(wavelength_excitation, wavelength_emission)
ax.plot_surface(X, Y, sum, cmap='viridis')
ax.set_xlabel('Excitation')
ax.set_ylabel('Emission')
ax.set_zlabel('Intensity')
plt.show()

#Точки для графика смещения
for i in range(111):
    print(str(270 + i * 3) + '  ' + str(sum[i][4]/4.285))
for i in range(77):
    print(str(250 + i * 3) + '  ' + str(sum[29][i]/4.743))