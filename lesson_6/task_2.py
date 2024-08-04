import math

def count_divisors(X):
    count = 0
    sqrt_X = int(math.sqrt(X))

    for i in range(1, sqrt_X + 1):
        if X % i == 0:
            count += 1 
            if i != X // i: 
                count += 1

    return count

X = int(input("Введите натуральное число X (x ≤ 2e9): "))

if X > 0 and X <= 2 * 10**9:
    print("Количество натуральных делителей числа", X, "равно:", count_divisors(X))
else:
    print("Число должно быть натуральным и не превышать 2e9.")