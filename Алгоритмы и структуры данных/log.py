from collections import Counter
for _ in range(int(input())):
    u = input(); c1 = Counter(input().split()); c1.subtract(Counter(input().split())); r = 0    
    for k in list(c1.keys()):
        if len(k) > 1: r += abs(c1[k]); c1[str(len(k))] += c1[k]; c1[k] = 0            
    print(r + (sum(c1[k] for k in c1.keys() if c1[k] > 0) * 2) - abs((c1["1"])))