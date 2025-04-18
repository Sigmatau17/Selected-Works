import math as mt
from scipy.integrate import quad
#Константы
R = 8.314
nu = 1
i = 3
P0 = 100000
V0 = 1
V1 = 1.0088
V2 = 0.6866
V3 = 2.9043
V4 = 2.7112
P1 = 98688.67
P2 = 160015.42
P3 = 269032.08
P4 = 132754.98
#Функции, ограничивающие цикл
def p1(v):
    return P0 * mt.exp(1.5*(V0-v))
def p2(v):
    return 2 * P0 * mt.atan(3*v/2*V0)
def p3(v):
    return P0 * mt.tan(3*v/2*V0)
def p4(v):
    return P0 * mt.atan(3*v/2*V0)

#Находим температуры в переходных точках
T1 = (P1 * V1) / (nu*R)
T2 = (P2 * V2) / (nu*R)
T3 = (P3 * V3) / (nu*R)
T4 = (P4 * V4) / (nu*R)

#Находим работу по каждому процессу и суммарную работу
a12 = quad(p1, 1.0088, 0.6866)[0]
a23 = quad(p2, 0.6866, 2.9043)[0]
a34 = quad(p3, 2.9043, 2.7112)[0]
a41 = quad(p4, 2.7112, 1.0088)[0]
a = round(a12 + a23 + a34 + a41, 2)

#Находим изменение внутренней энергии по каждому процессу
u12 = i/2 * nu * R * (T2 - T1)
u23 = i/2 * nu * R * (T3 - T2)
u34 = i/2 * nu * R * (T4 - T3)
u41 = i/2 * nu * R * (T1 - T4)

#Находим теплоту по каждому процессу, теплоту, полученную газом.
q12 = a12 + u12
q23 = a23 + u23
q34 = a34 + u34
q41 = a41 + u41
Q = []
Q.extend((q12, q23, q34, q41))
qr = 0
for i in range (len(Q)):
    if Q[i] > 0:
        qr = round(qr + Q[i], 2)
q = round(q12 + q23 + q34 + q41, 2)

#Находим КПД
ef = round(a/qr * 100, 2)

#Результаты
print('Работа, совершенная газом равна ' + str(a) + ' Дж')
print('Теплота, переданная газу в ходе цикла равна ' + str(qr) + ' Дж')
print('КПД цикла равен ' + str(ef) + ' %')