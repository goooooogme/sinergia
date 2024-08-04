word = input("Введите слово из маленьких латинских букв: ")

vowels = "aeiou"
vowel_count = {vowel: 0 for vowel in vowels}
consonant_count = 0

for char in word:
    if char in vowels:
        vowel_count[char] += 1
    elif char.isalpha() and char not in vowels:  
        consonant_count += 1

if all(vowel_count[vowel] > 0 for vowel in vowels):
    print("Количество согласных букв:", consonant_count)
    print("Количество каждой гласной буквы:")
    for vowel in vowels:
        print(f"{vowel}: {vowel_count[vowel]}")
else:
    print(False)