import random

# Генерируем список из 37 случайных значений "x" или "+"
random_values = [random.choice(["x", "+"]) for _ in range(37)]

# Выводим результат
print(random_values)