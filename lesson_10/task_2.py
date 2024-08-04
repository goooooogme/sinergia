my_dict = {}

for num in range(10, -6, -1):
    if num < 0:
        value = float(num ** num)
    else:
        value = num ** num

    my_dict[num] = value

print(my_dict)