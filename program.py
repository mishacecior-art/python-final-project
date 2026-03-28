def main():
    names = []
    levels = []

    while True:
        print("\n")
        print("1. Добавить игрока")
        print("2. Показать всех игроков")
        print("3. Удалить игрока")
        print("4. Поиск игрока по имени")
        print("5. Повысить уровень")
        print("6. Сортировка игроков")
        print("7. Выход")
        print()

        choice = input("Выбор: ")

        if choice == "1":
            add_player(names, levels)
        elif choice == "2":
            display_players(names, levels)
        elif choice == "3":
            remove_players(names, levels)
        elif choice == "4":
            search_players(names, levels)
        elif choice == "5":
            level_up(names, levels)
        elif choice == "6":
            sort_players(names, levels)
        elif choice == "7":
            break
        else:
            print("Неизвестная команда: ")

            
def add_player(names, levels):
    name = input("Введите имя игрока: ")
    level = int(input("Введите уровень игрока: ")) 

    names.append(name)
    levels.append(level)

    print(f"Игрок {name} успешно добавлен! ")

def display_players(names, levels):
    for i in range(len(names)):
        print(f"{i+1} {names[i]} - {levels[i]}")

    print()

def remove_players(names, levels):
    index = int(input("Введите номер игрока для удаления:"))

    remove_name = names.pop(index - 1)
    remove_level = levels.pop(index - 1)

    print(f"Игрок {remove_name} c уровнем {remove_level} был удалён: ")

def search_players(names, levels):
    search_name = input("Введите имя для поиска: ")

    found = False
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"Найден игрок {i+1} {names[i]} c уровнем {levels}: ")
            found = True

    if not found: 
        print("Игрок не найден: ")

def level_up(names, levels):
    player_id = int(input("Введите номер игрока для повышения уровня:"))
    player_id -= 1
    
    if player_id < 0 or player_id >= len(names):
        print("Игрок не найден: ")
        return
    
    increase_level = int(input("На сколько повысить уровень: "))
    levels[player_id] += increase_level

    print(f"Текущий уровень {names[player_id]} {levels[player_id]}")

def sort_players(names, levels):
    for i in range(len(levels)):
        for j in range(len(levels)-1-i):
            if levels[j] > levels[j+1]:
                levels[j], levels[j+1] = levels[j+1], levels[j]
                names[j], names[j+1] = names[j+1], names[j]

    print("Сортировка прошла: ")

main()
