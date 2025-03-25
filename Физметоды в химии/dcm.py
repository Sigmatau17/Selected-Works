import numpy as np
import matplotlib.pyplot as plt

wavelength_excitation = np.arange(250, 481, 3)  # Длины волн поглощения
wavelength_emission = np.arange(270, 603, 3)  # Длины волн эмиссии

to5 = np.loadtxt("to-5 dcm fluo.txt")
to5 = to5[:, 1:]

dcm = np.loadtxt("dcm fluo.txt")
dcm = dcm[:, 1:]

sum = to5 - dcm
to5[to5 < 0] = 0
to5[to5 > 25] = 0
max_index = np.unravel_index(np.argmax(to5, axis=None), to5.shape)
#to5[max_index[0]][max_index[1]] = 200
#to5[44][18]=200

# Построение 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(wavelength_excitation, wavelength_emission)
ax.plot_surface(X, Y, to5, cmap='viridis')
ax.set_xlabel('Excitation')
ax.set_ylabel('Emission')
ax.set_zlabel('Intensity')
plt.show()

#Точки для графика смещения
for i in range(111):
    print(str(270 + i * 3) + '  ' + str(to5[i][18]/23.18))
for i in range(77):
    print(str(250 + i * 3) + '  ' + str(to5[44][i]/23.62))