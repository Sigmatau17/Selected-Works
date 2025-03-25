import numpy as np
a = np.array([[[-3, -2, -3], [1, 3, 1], [0, -1, -4]], 
              [[0, 3, -3], [-4, -4, -2], [4, -2, 4]], 
              [[1, -3, 0], [0, 0, -1], [-2, -1, 0]]])
shape = (3)
c = np.zeros(shape)
for m in range(3):
    for p in range(3):
        c[m] += a[m][p][p]
print(c)