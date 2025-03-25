from sys import stdin
lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
for i in range(int(lines[0])):
    string = str(lines[2 * i + 2])
    brackets = []
    for i in string:
        brackets.append(i)
    s = 0
    ans = 0
    j = 0
    while j <= len(brackets) - 1:
        k = 0
        while k <= j:
            if brackets[k] == '(':
                s = s + 1
            else:
                s = s - 1
            k = k + 1
        if s < 0:
            ans = ans + 1
            brackets.append(brackets[j])
            brackets.remove(brackets[j])
            j = 0
        else:
            ans = ans + 0
            j = j + 1
        s = 0
    print(ans)