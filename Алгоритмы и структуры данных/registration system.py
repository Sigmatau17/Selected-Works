from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
lines.pop(0)
names = {}
for i in range(len(lines)):
    if lines[i] in names:
        names[lines[i]] += 1
        print(lines[i] + str(names.get(lines[i])))
    else:
        names[lines[i]] = 0
        print("OK")