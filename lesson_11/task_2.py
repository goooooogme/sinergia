import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return 'года'
    else:
        return 'лет'

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} добавлен с ID {new_id}.")

def read(ID):
    pet_info = get_pet(ID)
    if pet_info:
        name = list(pet_info.keys())[0]
        pet = pet_info[name]
        suffix = get_suffix(pet["Возраст питомца"])
        print(f"Это {pet['Вид питомца']} по кличке \"{name}\". Возраст питомца: {pet['Возраст питомца']} {suffix}. Имя владельца: {pet['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден.")

def update(ID):
    pet_info = get_pet(ID)
    if pet_info:
        name = list(pet_info.keys())[0]
        print(f"Обновляем информацию о питомце {name}.")
        pet_type = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")
        
        pets[ID] = {
            name: {
                "Вид питомца": pet_type,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print(f"Информация о питомце {name} обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} удален.")
    else:
        print("Питомец с таким ID не найден.")

def pets_list():
    for ID, info in pets.items():
        name = list(info.keys())[0]
        pet = info[name]
        suffix = get_suffix(pet["Возраст питомца"])
        print(f"ID {ID}: Это {pet['Вид питомца']} по кличке \"{name}\". Возраст питомца: {pet['Возраст питомца']} {suffix}. Имя владельца: {pet['Имя владельца']}")

def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
        if command == 'stop':
            break
        elif command == 'create':
            create()
        elif command == 'read':
            ID = int(input("Введите ID питомца: "))
            read(ID)
        elif command == 'update':
            ID = int(input("Введите ID питомца: "))
            update(ID)
        elif command == 'delete':
            ID = int(input("Введите ID питомца: "))
            delete(ID)
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()