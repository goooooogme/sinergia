def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1.intersection(set2)
    
    return len(common_elements)

n1 = int(input("N1: ")) 
list1 = [int(input("Числа: ")) for _ in range(n1)] 

n2 = int(input("N2: "))  
list2 = [int(input("Числа: ")) for _ in range(n2)] 

result = count_common_elements(list1, list2)

print(result)