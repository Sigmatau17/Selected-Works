import sys

# Чтение данных
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

# Функция для построения бинарного дерева и нахождения предков вершин
def find_ancestors(sequence):
    root = sequence[0]
    ancestors = []
    for i in range(1, len(sequence)):
        current = root
        while True:
            if sequence[i] > current:
                if 2 * current + 1 not in ancestors:
                    ancestors.append(2 * current + 1)
                    break
                else:
                    current = 2 * current + 1
            else:
                if 2 * current not in ancestors:
                    ancestors.append(2 * current)
                    break
                else:
                    current = 2 * current
    return ancestors

# Находим предков для каждой вершины, кроме корня
result = find_ancestors(sequence[1:])

# Выводим результат
print(' '.join(map(str, result)))

