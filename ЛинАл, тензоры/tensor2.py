import numpy as np
a = np.array([[[2, 6, -6], [1, -5, 5], [-3, 1, 1]], 
              [[3, 3, -2], [4, -3, -3], [-2, 6, 5]], 
              [[-4, 2, 0], [1, -1, 5], [4, -4, -2]]])
b = np.array([[-2, -6, -6], [4, -3, 5], [1, -4, 0]])
c = np.array([[2, -3, 4], [4, 1, -3], [1, 4, -5]])
shape = (3)
d = np.zeros(shape)
for i in range(3):
    for k in range(3):
        for j in range(3):
            for l in range(3):
                d[l] += a[j][i][k] * b[j][i] * c[k][l]
print(d)