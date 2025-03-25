import sys

n, I = map(int, input().split())
I *= 8
k = I // n
maxValues = 2 ** k

soundFile = list(map(int, input().split()))
soundFile.sort()

frequencies = []
count = 1
for i in range(n):
    if i == n - 1 or soundFile[i] != soundFile[i + 1]:
        frequencies.append(count)
        count = 1
    else:
        count += 1

totalUnique = len(frequencies)
left = right = currentSum = maxSum = 0
while right < totalUnique:
    if right - left < maxValues:
        currentSum += frequencies[right]
        right += 1
    else:
        currentSum -= frequencies[left]
        left += 1
    maxSum = max(maxSum, currentSum)

print(n - maxSum)
