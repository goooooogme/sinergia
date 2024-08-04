import math

def factorial(n):
    return math.factorial(n)

def factorial_list(n):

    fact_n = factorial(n)

    result = []
    for i in range(fact_n, 0, -1):
        result.append(factorial(i))
    
    return result

n = int(input("Введите натуральное число: "))
result_list = factorial_list(n)
print(result_list)