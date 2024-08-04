def rearrange_array(N, numbers):
    rearranged = []
    for i in range(N):
        if i % 2 == 0:
            rearranged.append(numbers[N - 1 - i // 2])
        else:
            rearranged.append(numbers[i // 2])
    
    return rearranged

N = int(input("Введите число N:"))

numbers = list(map(int, input("Введите числа: ").split()))

result = rearrange_array(N, numbers)

print(" ".join(map(str, result)))