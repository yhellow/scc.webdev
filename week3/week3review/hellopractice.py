num = 'straight'
print(num)


def fct(i):
    return i + 1


print(fct(2))


def sum_all(a, b, c):
    return a + b + c


def mul(a, b):
    return a * b


result = sum_all(1, 2, 3) + mul(10, 10)

print(result)


def minus(a, b):
    return a - b


result2 = minus(mul(10, 10), sum_all(1, 2, 3))
print(result2)
