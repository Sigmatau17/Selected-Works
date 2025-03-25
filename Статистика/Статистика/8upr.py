import numpy as np
file = open("calls", "r")
vyborka = []
for i in range(10000):
    number = float(file.readline())
    vyborka.append(number)
sum = 0
for i in range(len(vyborka)):
    sum = sum + vyborka[i]
mo = sum/10000
print(mo)
disp = 0
for i in range(len(vyborka)):
    disp = disp + np.power(vyborka[i] - mo, 2)/10000
sum = 0
print(mo - np.sqrt(3*disp))
print(mo + np.sqrt(3*disp))
print(sorted(vyborka))