def print_even_numbers(A, B):
    if A > B:
        print("Некорректный диапазон. A должно быть меньше или равно B.")
        return

    if A % 2 != 0:
        A += 1
    
    even_numbers = [str(num) for num in range(A, B + 1, 2)]
    print(" ".join(even_numbers))

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

print_even_numbers(A, B)