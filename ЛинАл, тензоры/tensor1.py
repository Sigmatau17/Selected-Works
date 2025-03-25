import numpy as np
a = np.array([[[-2, 1], [3, -2]], [[-3, -2], [4, 3]]])
b = np.array([[[-1, -3], [-2, 3]], [[2, 2], [-3, -4]]])
shape = (2, 2, 2, 2)
c = np.zeros(shape)
for m in range(2):
    for r in range(2):
        for k in range(2):
            for p in range(2):
                for t in range(2):
                    c[k][t][p][m] += a[k][m][r] * b[t][p][r]
print(c)