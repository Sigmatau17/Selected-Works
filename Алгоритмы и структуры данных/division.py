from sys import stdin
"""
def sumOfDivPow(array):
    dividers = {}
    for number in array:
        i = 2
        while i * i <= number:
            while number % i == 0:
                divider = dividers.get(i, 0)
                dividers[i] = divider + 1
                number //= i
            i += 1
        if number != 1:
            divider = dividers.get(number, 0)
            dividers[number] = divider + 1
    return posibility(dividers.values(), len(array))

def posibility(dictionary, len_array):
    for power in dictionary:
        if power % len_array != 0:
            return False
        else:
            return True
"""
def calculate(a):
    divisors = {}

    for num in a:
        i = 2
        while i * i <= num:
            while num % i == 0:
                value_divisor = divisors.get(i, 0)
                divisors[i] = value_divisor + 1
                num //= i
            i += 1
        if num != 1:
            value_divisor = divisors.get(num, 0)
            divisors[num] = value_divisor + 1

    return check_on_full_match(divisors.values(), len(a))

def check_on_full_match(collection, length_array):
    for num in collection:
        if num % length_array != 0:
            return False
    return True

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
ans = []
for i in range(int(lines[0])):
    string = str(lines[2 * i + 2])
    array = list(map(int, string.split()))
    result = "YES" if calculate(array) else "NO"
    ans.append(result)
print("\n".join(ans))