import numpy as np
shape = (3, 3, 3)
a = np.zeros(shape)
for t in range(3):
    for l in range(3):
        for i in range(3):
            a[i][t][l] = (t+1) - 2*(l+1) - 3*(i+1)
print(a)