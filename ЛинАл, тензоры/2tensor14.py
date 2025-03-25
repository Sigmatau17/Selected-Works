import numpy as np
a = np.array([[[-2, -3, -1], [-5, -5, -5], [-2, -5, -1]], 
              [[0, -4, 6], [4, 0, 2], [6, -1, 6]], 
              [[-2, -5, -1], [-4, -4, 1], [-5, 2, -6]]])
shape = (3, 3, 3)
b = np.zeros(shape)
for i in range(3):
    for m in range(3):
        for l in range(3):
            b[l][m][i] = a[i][l][m]
print(b)