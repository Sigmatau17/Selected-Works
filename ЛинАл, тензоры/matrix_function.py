import numpy as np
from scipy.linalg import expm
a = np.array([[3, -1, 0], [6, -3, 2], [8, -6, 5]])
e = np.eye(3)

b = np.linalg.matrix_power(a, 7) - 5 * np.linalg.matrix_power(a, 6) 
+ 2 * np.linalg.matrix_power(a, 5) + 41 * np.linalg.matrix_power(a, 4) 
- 105 * np.linalg.matrix_power(a, 3) + 69 * np.linalg.matrix_power(a, 2) + 63 * a - 65 * e

print(b)

a = np.array([[4, 2, -5], [6, 4, -9], [5, 3, -7]])

print(expm(a))