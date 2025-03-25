import math
x = 1
a = 0
for i in range(0,6):
    a += x**i/math.factorial(i)
print(a)