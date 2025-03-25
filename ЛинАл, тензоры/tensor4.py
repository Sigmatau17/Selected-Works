import numpy as np
a = np.array([[[0, -2], [-4, -1]], [[-4, 4], [3, -1]]])
b = np.array([[4, 1], [-1, -2]])
c = np.tensordot(a, b, axes=0)
print(c)