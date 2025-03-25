from sys import stdin

def count_steps_to_match(a, b):
    n = len(a)
    steps = 0
    a_count = {}
    b_count = {}
    swap_indices = []

    for i in range(n):
        if a[i] not in a_count:
            a_count[a[i]] = 1
        else:
            a_count[a[i]] += 1

        if b[i] not in b_count:
            b_count[b[i]] = 1
        else:
            b_count[b[i]] += 1

    if a_count != b_count:
        return -1

    for i in range(n):
        if a[i] != b[i]:
            j = i + 1
            while b[j] != a[i]:
                j += 1
            while j > i:
                b[j], b[j-1] = b[j-1], b[j]
                swap_indices.append(str(j) + ' ' + str(j+1))
                j -= 1
                steps += 1

    return steps, swap_indices

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
n = int(lines[0])
a = list(map(int, str(lines[1]).split()))
b = list(map(int, str(lines[2]).split()))
steps, swap_indices = count_steps_to_match(a, b)
print(steps)
for i in range(len(swap_indices)):
    print(swap_indices[i])