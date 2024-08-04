number = int(input("Введите пятизначное целое число: "))

if 10000 <= number <= 99999:
    units = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    ten_thousands = (number // 10000) % 10

    result = (tens ** units) * hundreds / (ten_thousands - thousands)

    print(f"Результат: {result:.1f}")
else:
    print("Ошибка: введено не пятизначное число.")