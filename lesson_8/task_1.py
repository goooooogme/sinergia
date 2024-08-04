N = int(input("Введите число N: "))

numbers = []

for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

reversed_numbers = numbers[::-1]

print(" ".join(map(str, reversed_numbers)))