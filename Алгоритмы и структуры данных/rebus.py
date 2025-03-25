import math as mt
line = str(input())
symbols = list(map(str, line.split()))
n = int(symbols[len(symbols) - 1])
symbols.pop(len(symbols) - 1)
symbols.pop(len(symbols) - 1)
pm = [1]
for i in range(len(symbols)):
    if symbols[i] == '+':
        pm.append(1)
    elif symbols[i] == '-':
        pm.append(-1)
pos = 0
neg = 0
for i in range(len(pm)):
    if pm[i] == 1:
        pos = pos + 1
    else:
        neg = neg + 1
max_val = n * pos - neg
min_val = pos - n * neg
if n <= max_val and n >= min_val:
    below_max = max_val - n
    ans = ""
    for i in range(len(pm)):
        delta = min(n - 1, below_max)
        below_max -= delta
        if pm[i] == 1:
            if i != 0:
                ans += " + "
            ans += str(n - delta)
        else:
            ans += " - " + str(1 + delta)
    ans += " = " + str(n)
    print("Possible")
    print(ans)
else:
    print("Impossible")

    """print("Possible")
    k = 1
else:
    print("Impossible")
    k = 0
if k == 1:
    numbers = []
    s = 0
    while len(pm) != 1:
        x = pm[0]
        pos_left = 0
        neg_left = 0
        for i in range(len(pm)):
            if pm[i] == 1:
                pos_left = pos_left + 1
            else:
                neg_left = neg_left + 1
        max_left = s + n * pos_left - neg_left
        min_left = s + pos_left - n * neg_left
        while abs(x) <= n:
            if n <= max_left and n >= min_left:
                numbers.append(x)
                s = s + x
                pm.pop(0)
                break
            else:
                x = pm[0] * (abs(x) + 1)
    sign = ['+']
    for i in range(len(symbols)):
        if symbols[i] == '+' or symbols[i] == '-':
            sign.append(symbols[i])
    numbers.append(n - sum(numbers))
    ans = ''
    for i in range(len(numbers)):
        ans  = ans + sign[i] + ' ' + str(abs(numbers[i])) + ' '
    ans = ans + '= ' + str(n)
    ans = ans[2:]
    print(ans)"""