import math
a = 1
b = 1
n = 1
while (b <= a):
    a = (a)/(1 + n*a)
    b = 1/(math.pow((n+1), 1.5))
    n = n + 1
    print(n)
