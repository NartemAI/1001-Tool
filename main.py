import functions

programs = {
    1: ("Монетка", functions.coin_flip),
    2: ("Проверка на простое число", functions.Checking_a_prime_number),
    3: ("Калькулятор НОК и НОД", functions.LCM_GCD),
    4: ("Текст в двоичный код", functions.text_to_binary),
    5: ("Калькулятор ИМТ", functions.BMI),
    6: ("Таймер выключения", functions.shutdown_timer),
    7: ("Генерация пароля", functions.generate_password),
    8: ("Проверка пароля", functions.check_password),
    9: ("Генерация логина", functions.generate_login),
    10: ("Генератор случайных чисел", functions.random_number),
    11: ("Калькулятор Hm", functions.torque_calculator),
    12: ("Ip check", functions.ip_check),
}


def show_main_instructions():
    print("\t* Нажмите Enter для закрытия окна")
    print("\t* Введите 0 для просмотра программ")


def show_programs():
    print("Для выбора программы введите соответствующее число")
    print("0 - выйти в главное меню")
    print("S - поиск программы 🔍")
    for key, (name, _) in programs.items():
        print(f"{key} - {name}")

def search_program():
    print("Введите название программы (или часть названия):")
    query = input("#$ ").strip().lower()
    if not query:
        print("Поиск отменён")
        return
    found = False
    for key, (name, _) in programs.items():
        if query in name.lower():
            print(f"{key} - {name}")
            found = True
    if not found:
        print("Ничего не найдено ❌")


print("Здравствуйте! Здесь вы найдёте много интересных программ!")
show_main_instructions()

while True:
    i = input("#$ ")
    if i == "":
        break

    if i == "0":  # меню программ
        while True:
            show_programs()
            choice = input("#$ ").strip()

            if choice == "":
                break
            if choice == "0":
                break
            if choice.lower() == "s":
                search_program()
                continue

            if choice.isdigit():
                choice = int(choice)
                if choice in programs:
                    programs[choice][1]()  # вызов функции из словаря
                else:
                    print("Такой программы нет!🤷")
            else:
                print("Введите корректное число или S для поиска!")

        show_main_instructions()

    elif i.isdigit():
        i = int(i)
        if i in programs:
            programs[i][1]()  # вызов функции напрямую
        else:
            print("Такой программы нет!🤷")
        show_main_instructions()
    else:
        print("Введите корректное число!")
        show_main_instructions()
