import numpy as np
file = open("test", "r")
vyborka = []
v = 500
for i in range(v):
    number  = float(file.readline())
    vyborka.append(number)
sort = sorted(vyborka)
sum = 0
for i in range(v):
    sum = sum + sort[i]
ex = sum/v
print(ex)
sum = 0
for i in range(v):
    sum = sum + np.power(sort[i] - ex, 2)
dx = sum/v
dx0 = v/(v-1) * dx
print(dx0)
gist = []
g = 10
k = (sort[v-1] - sort[0])/g
coloumn = []
for i in range(g):
    for j in range(v):
        if sort[j] >= sort[0] + i*k and sort[j] < sort[0] + (i+1)*k:
            coloumn.append(sort[j])
    gist.append(len(coloumn))
    coloumn.clear()
print(gist)
print(sort[0])
print(sort[v-1])