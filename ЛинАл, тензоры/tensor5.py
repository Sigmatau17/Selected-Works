import numpy as np
shape = (2, 2, 2, 2, 2)
a = np.zeros(shape)
for r in range(2):
    for i in range(2):
        for j in range(2):
            for n in range(2):
                for t in range(2):
                    a[t][j][n][r][i] = -2*(r+1)-5*(i+1)+5*(j+1)-4*(n+1)-4*(t+1)

shape = (2)
c = np.zeros(shape)
for j in range(2):
    for n in range(2):
        for t in range(2):
            c[t] += a[t][j][n][n][j]
print(c)