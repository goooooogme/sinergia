number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
elif number % 2 == 0: 
    if number > 0:
        print("положительное четное число")
    else:
        print("отрицательное четное число")
else:
    print("число не является четным")