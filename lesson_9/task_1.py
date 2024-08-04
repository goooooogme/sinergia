def count_unique_numbers(n, numbers):
    unique_numbers = set(numbers) 
    return len(unique_numbers)  

n = int(input("N: "))  
numbers = list(map(int, input("Числа: ").split()))  

result = count_unique_numbers(n, numbers)

print(result)