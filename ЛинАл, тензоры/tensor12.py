import numpy as np
a = np.array([[[0, -1], [-2, 3]], [[-4, -6], [-2, 3]]])
v1 = np.array([-6, 3])
v2 = np.array([-5, 5])
u1 = np.array([2, -2])

f = 0
for r in range(2):
    for t in range(2):
        for n in range(2):
            f += a[n][r][t] * u1[n] * v1[t] * v2[r]
print(f)