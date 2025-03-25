import math as mt
n = int(input())
sum = n + (n - 1)
list = list(str(sum))
counter = 0
for i  in range(len(list)):
    if list[i] == str(9):
        counter = counter + 1
if sum < 9:
    a = 0
    print(int(mt.factorial(n)/(mt.factorial(2) * mt.factorial(n - 2))))
elif counter == len(list):
    a = 1
    print(a)
else:
    cur = []
    answer = 0
    for i in range(9):
        cur.append(int(str(i) + (len(list) - 1) * '9'))
    for i in range(len(cur)):
        if cur[i] <= n:
            answer = answer + (cur[i] // 2)
        elif cur[i] > n and cur[i] <= sum:
            answer = answer + ((n - (cur[i] - n) + 1) / 2)
        else:
            answer = answer + 0
    print(int(answer))