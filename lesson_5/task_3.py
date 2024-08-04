X = float(input("Введите минимальную сумму инвестиции: "))
A = float(input("Введите сумму, которая есть у Майкла: "))
B = float(input("Введите сумму, которая есть у Ивана: "))

if A >= X and B >= X:
    print(2) 
elif A >= X:
    print("Mike") 
elif B >= X:
    print("Ivan") 
elif A + B >= X:
    print(1)
else:
    print(0) 