import math
import random

In = open('input.txt', 'r')
n = int(In.readline())
r = int(In.readline())
a = float(In.readline())
b = int(In.readline())
t = float(In.readline())
In.close()
if n < 2:
    Out = open('output.txt', 'w+')
    Out.write(str("I won't do it..."))
    Out.close()
deltax = (b-a)/(n-1)
if t < 0 or t > 1:
    Out = open('output.txt', 'w+')
    Out.write(str("I won't do it..."))
    Out.close()
if r == 1:
    t = 1
if r == 2:
    t = 0
if r == 3:
    t = 0.5
if r == 4:
   t = random.random() 
points = []
for i in range (n-1):
    p = math.pow(2, (a + i * deltax + t * deltax))
    points.append(p)
sum = 0
for i in points:
    sum += i
Sigma = round(sum * deltax, 5)
Out = open('output.txt', 'w+')
Out.write("The integral sum is " + str(Sigma))
Out.close()