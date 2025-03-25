import matplotlib as plt
import numpy as np
p = (10**7) * 6 * (10**(-30))
k = 1.38 * 10**(-23)
T = 273
def L(x):
    return (np.exp((p * x)/(k*T))+np.exp(-(p * x)/(k*T)))/(np.exp((p * x)/(k*T))-np.exp(-(p * x)/(k*T))) - 1/((p * x)/(k*T))
E = np.arange(0, 1000, 0.01)
plt.plot(E, p/E)
plt.xlabel(r'$E$')
plt.ylabel(r'$a$')
plt.title(r'$$')
plt.grid(True)
plt.show()