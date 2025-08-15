# Написать программу с использованием языка программирования Python, которая будет генерировать последовательность 
# случайных чисел до тех пор, пока пользователь не введёт ноль. Вывести на экран все числа, кроме последнего.

import random

def generate_until_zero():
    numbers = []

    while True:
        random_number = random.randint(1, 100)
        print(f"Случайное число: {random_number}")

        user_input = int(input("Введите число (0 для выхода): "))

        if user_input == 0:
            break
        numbers.append(user_input)

    print("Вы ввели числа (кроме 0):")
    print(numbers)


if __name__ == "__main__":
    generate_until_zero()