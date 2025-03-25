import math

In = open('input.txt', 'r')
ship = str(In.readline())
shipcrd = list(map(float, ship.split()))
scx = shipcrd[0]
scy = shipcrd[1]
keel = str(In.readline())
keelcrd = list(map(float, keel.split()))
kcx = keelcrd[0]
kcy = keelcrd[1]
mast = str(In.readline())
mastcrd = list(map(float, mast.split()))
mcx = mastcrd[0]
mcy = mastcrd[1]
enemy = str(In.readline())
enemycrd = list(map(float, enemy.split()))
ecx = enemycrd[0]
ecy = enemycrd[1]
In.close()

"Угол наклона мачты"
cosgamma = (1/(math.sqrt(mcx**2 + mcy**2 + 1)))
gamma = round(math.degrees(math.acos(cosgamma)), 2)

"Z координата киля"
kcz = (-kcx * mcx - kcy * mcy)

"Левая пушка"
lgcx = mcy * kcz - kcy 
lgcy = -(mcx * kcz - kcx)
lgcz = mcx * kcy -mcy * kcx

"Правая пушка"
rgcx = kcy - kcz * mcy
rgcy = -(kcx - kcz * mcx)
rgcz = kcx * mcy - kcy * mcx

"Вектор, определяющий положение врага относительно корабля"
escx = ecx - scx
escy = ecy - scy
escz = (-escx * mcx - escy * mcy)

"Угол teta - угол между килем и вектором, определяющим положение врага относительно корабля "
costeta = round((escx * kcx + escy * kcy + escz * kcz)/(math.sqrt(escx**2 + escy**2 + escz**2) * math.sqrt(kcx**2 + kcy**2 + kcz**2)), 2)
teta = math.degrees(math.acos(costeta))
beta = round((90 - teta), 2)

"Нормаль к борту(левому)"
ncx = -kcy
ncy = kcx

"Угол, определюящий борт"
costau = round((escx * ncx + escy * ncy)/(math.sqrt(escx**2 + escy**2) * math.sqrt(ncx**2 + ncy**2)), 2)
            
Out = open('output.txt', 'w+')
if beta > 60 or beta < -60 or escz < 0:
    Out.write(str(0))
    Out.write(str('\n' + str(0)))
elif costau > 0:
    Out.write(str(1))
    Out.write(str('\n' + str(beta)))
elif costau < 0:
    Out.write(str(-1))
    Out.write(str('\n' + str(beta)))
else:
    Out.write(str(0))
    Out.write(str('\n' + str(0)))

Out.write(str('\n' + str(gamma)))
Out.write(str('\n' + "Good luck on tests!"))
Out.close()