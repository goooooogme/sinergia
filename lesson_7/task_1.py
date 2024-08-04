def is_palindrome(s):
    return s == s[::-1]

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("yes")
else:
    print("no")