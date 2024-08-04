def check_numbers(sequence):
    seen = set() 
    results = [] 

    for number in sequence:
        if number in seen:
            results.append("YES")
        else:
            results.append("NO")
            seen.add(number)
    
    return results

input_line = input().strip()  
numbers = input_line.split()  


numbers = [int(num) for num in numbers]

results = check_numbers(numbers)

for result in results:
    print(result)