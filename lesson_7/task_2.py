def normalize_spaces(s):
    return ' '.join(s.split())

input_string = input("Введите строку: ")

output_string = normalize_spaces(input_string)

print(output_string)