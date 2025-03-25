def permutation(prefix, str):
    length = len(str)
    if length == 0:
        rule(prefix)
    else:
        for i in range(length):
            permutation(prefix + str[i], str[:i] + str[i+1:])

def rule(prefix):
    arrayOfPermutes = [0] * n
    for i in range(n):
        element = ""
        for j in range(k):
            index = int(prefix[j])
            element += digits[i][index]
        arrayOfPermutes[i] = int(element)
    
    min_val = float('inf')
    max_val = float('-inf')
    for i in range(n):
        min_val = min(min_val, arrayOfPermutes[i])
        max_val = max(max_val, arrayOfPermutes[i])
    
    global minRes
    minRes = min(abs(max_val - min_val), minRes)

n, k, minRes = map(int, input().split())
permutes = ""
digits = [''] * 8

for i in range(k):
    permutes += str(i)

for i in range(n):
    digits[i] = input()

permutation("", permutes)

print(minRes)
