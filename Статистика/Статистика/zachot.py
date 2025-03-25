import numpy as np
file = open("test", "r")
vyborka = []
print("Введите объем выборки")
v = int(input())
for i in range(v):
    number = float(file.readline())
    vyborka.append(number)
sort = sorted(vyborka)
sum = 0
for i in range(v):
    sum = sum + vyborka[i]
ex = sum/v
print(ex) #Среднее выборочное, то есть X с черточкой
sum = 0
for i in range(v):
    sum = sum + (vyborka[i] - ex)**2
dx = sum/v
dx0 = v/(v-1) * dx
print(dx0) #Несмещенная выборочная дисперсия, то есть S0
gist = []
print("Введите колчество столбцов гистограммы")
g = int(input())
k = (sort[v-1] - sort[0])/g
coloumn = []
for i in range(g):
    for j in range(v):
        if sort[j] >= sort[0] + i * k and sort[j] < sort[0] + (i+1) * k:
            coloumn.append(sort[j])
    gist.append(len(coloumn))
    coloumn.clear()        
print(gist) #Количество чисел, попавших в столбцы гистограммы
print(ex - 1.964729 * dx0/np.sqrt(500))
