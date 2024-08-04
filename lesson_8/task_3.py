def minimum_boats_needed(m, n, weights):
    weights.sort() 
    i, j = 0, n - 1  
    boats = 0 

    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1  
        j -= 1  
        boats += 1  

    return boats

m = int(input("M: "))
n = int(input("N: "))
weights = [int(input("Weights: ")) for _ in range(n)]

result = minimum_boats_needed(m, n, weights)

print(result)