import numpy as np
file = open("zp", "r")
vyborka = []
for i in range(81):
    number = float(file.readline())
    vyborka.append(number)
print(sorted(vyborka))
sum = 0
for i in range(len(vyborka)):
    sum = sum + vyborka[i]
mo = sum/81
print(mo)
disp = 0
for i in range(len(vyborka)):
    disp = disp + np.power(vyborka[i] - mo, 2)/81
ndisp = disp * (81/80)
print(disp)
print(ndisp)
zp = []
for i in range(len(sorted(vyborka))):
    if sorted(vyborka)[i] >= 70817.2 and sorted(vyborka)[i] < 78528.4:
        zp.append(sorted(vyborka)[i])
print(len(zp))