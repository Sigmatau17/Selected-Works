import numpy as np
a = np.array([[-2, 4], [6, 0]])
b = np.array([[3], [5]])
c = np.array([3, -5])
d = np.array([-1])
e = np.array([[1, 6], [-6, -1]])


g = np.tensordot(b, c, axes=0)
g = -4 * g
print(g)
h = np.tensordot(d, e, axes=0)
h = -5 * h
print(h)
z = g + h
print(z)
f = np.tensordot(a, z, axes=0)
print(f)