import math as mt
from scipy.integrate import quad
P0 = 100000
V0 = 1
DP = 10000
A = 2
B = 100000
R = 8.314
nu = 1
i = 3
P1 = 94756.1
P2 = P1
V1 = 0.331
V2 = 1.669
def p1(v):
    return P0 + DP * mt.cos(2 * mt.pi * A * (v -V0))  
def p2(v):
    return 0.5 * P0 + B * mt.pow(v - V0, 2)
#Находим температуры в переходных точках
T1 = (P1 * V1) / (nu*R)
T2 = (P2 * V2) / (nu*R)

#Находим работу по каждому процессу и суммарную работу
a12 = quad(p1, V1, V2)[0]
a21 = quad(p2, V2, V1)[0]
a = round(a12 + a21, 2)

#Находим изменение внутренней энергии по каждому процессу
u12 = i/2 * nu * R * (T2 - T1)
u21 = i/2 * nu * R * (T1 - T2)

#Находим теплоту по каждому процессу, теплоту, полученную газом.
q12 = a12 + u12
q21 = a21 + u21
Q = []
Q.extend((q12, q21))
qr = 0
for i in range (len(Q)):
    if Q[i] > 0:
        qr = round(qr + Q[i], 2)
q = round(q12 + q21, 2)

#Находим КПД
ef = round(a/qr * 100, 2)

#Результаты
print('КПД цикла равен ' + str(ef) + ' %')