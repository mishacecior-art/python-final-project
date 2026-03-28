def main():
    names = []
    levels = []

    while True:
        print("1. Добавить игрока")
        print("2. Показать всех игроков")
        print("3. Удалить игрока")
        print("4. Поиск игрока по имени")
        print("5. Повысить уровень")
        print("6. Сортировка игроков")
        print("7. Выход")

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
    remove_name = names.pop(index)
    remove_level = levels.pop(index)
    print(f"Игрок {remove_name} c уровнем {remove_level} был удалён: ")

def search_players(names, levels):
    pass

def level_up(names, levels):
    pass
    
def sort_players(names, levels):
    pass

main()
