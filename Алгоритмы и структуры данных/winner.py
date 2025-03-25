"""from sys import stdin

def find_winner(dict):
    max_score = max(value[0] for value in dict.values())
    winner = next(key for key, value in dict.items() if value[0] == max_score and value[1] == min(val[1] for val in dict.values() if val[0] == max_score))
    return winner
lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
lines.pop(0)
steps = {}
for i in range(len(lines)):
    array = list(map(str, str(lines[i]).split()))
    name, score = array[0], int(array[1])
    if name in steps:
        steps[name][i][0] = score
        steps[name][i][1] = i+1
    else:
        steps[name] = [[score, i+1]]
print(steps)
print(find_winner(steps))
"""
d,r={},[]
for _ in ' '*int(input()): x,c=input().split();d[x]=d.get(x,0)+int(c);r+=[(d[x],x)]
m=max(d.values())
print([x for v,x in r if d[x]==m and v>=m][0])
