import numpy as np
a = np.array([[[[[3, -4], [3, 1]], [[0, 1], [0, 1]]], [[[3, 3], [2, 3]], [[-1, -4], [-2, -2]]]],
               [[[[-3, -3], [0, -3]], [[-3, -2], [-1, 3]]], [[[-3, 0], [-2, 0]], [[-2, -3], [3, 0]]]]])
shape = (2)
c = np.zeros(shape)
for m in range(2):
    for l in range(2):
        for p in range(2):
            c[m] += a[p][m][l][p][l]
print(c)