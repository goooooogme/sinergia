pets = {}

pet_name = input("Введите имя питомца: ")
pet_species = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

if 10 <= pet_age % 100 <= 20:
    age_suffix = "лет"
else:
    if pet_age % 10 == 1:
        age_suffix = "год"
    elif pet_age % 10 in (2, 3, 4):
        age_suffix = "года"
    else:
        age_suffix = "лет"

pets[pet_name] = {
    'Вид питомца': pet_species,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

pet_info = f'Это {pet_species.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}'

print(pet_info)