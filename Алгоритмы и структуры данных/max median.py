def find_max_median(a, n, k):
    l, r = 1, n
    while l < r:
        m = (l + r + 1) // 2
        if check(a, n, k, m):
            l = m
        else:
            r = m - 1
    return l

def check(a, n, k, m):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if a[i - 1] >= m else -1)
    
    min_prefix_sum = 0
    for i in range(k, n + 1):
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k])
        if prefix_sum[i] - min_prefix_sum > 0:
            return True
    return False

# Чтение входных данных
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Вызов функции и вывод результата
result = find_max_median(a, n, k)
print(result)
