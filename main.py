import functions

# Словарь с названиями функций
name_functions = {
    0: "Список программ",
    1: "Монетка",
    2: "Проверка на простое число",
    3: "Калькулятор НОК и НОД",
    4: "Текст в двоичный код",
    5: "Калькулятор ИМТ",
    6: "Таймер выклюючения",
    7: "Генерация пароля",
    8: "Проверка пароля",
    9: "Генерация логина"
}

kol_functions = len(name_functions)


def show_main_instructions():
    print("\t* Нажмите Enter для закрытия окна")
    print("\t* Введите 0 для просмотра программ")  # осталось только это


print("Здраствуйте! Здесь вы найте очень много интересных, веселых и нужных программ!")
show_main_instructions()

while True:
    i = input("#$ ")
    if i == "":
        break
    try:
        i = int(i)
    except ValueError:
        print("Введите корректное число!")
        continue

    if i == 0:
        # Меню просмотра списка программ
        while True:
            print("Для выбора программы введите соответствующее число")
            print("0 - выйти в главное меню")
            for key in name_functions:
                if key != 0:
                    print(f"{key} - {name_functions[key]}")
            choice = input("#$ ")
            if choice == "":
                break
            try:
                choice = int(choice)
            except ValueError:
                print("Введите корректное число!")
                continue

            if choice == 0:
                break
            elif choice == 1:
                functions.coin_flip()
            elif choice == 2:
                functions.Checking_a_prime_number()  # добавьте сюда вашу функцию
            elif choice == 3:
                functions.LCM_GCD()
            elif choice == 4:
                functions.text_to_binary()
            elif choice == 5:
                functions.BMI()
            elif choice == 6:
                functions.shutdown_timer()
            elif choice == 7:
                functions.generate_password()
            elif choice == 8:
                functions.check_password()
            elif choice == 9:
                functions.generate_login()
            else:
                print("Такой программы нет!🤷")
        show_main_instructions()  # показываем инструкции снова после выхода из подменю
    elif i == 1:
        functions.coin_flip()
        show_main_instructions()  # показываем инструкции после выполнения функции
    elif i == 2:
        functions.Checking_a_prime_number()  # добавьте сюда вашу функцию
        show_main_instructions()  # показываем инструкции после выполнения функции
    elif i == 3:
        functions.LCM_GCD()
        show_main_instructions()
    elif i == 4:
        functions.text_to_binary()
        show_main_instructions()
    elif i == 5:
        functions.BMI()
        show_main_instructions()
    elif i == 6:
        functions.shutdown_timer()
        show_main_instructions()
    elif i == 7:
        functions.generate_password()
        show_main_instructions()
    elif i == 8:
        functions.check_password()
        show_main_instructions()
    elif i == 9:
        functions.generate_login()
        show_main_instructions()
    else:
        print("Такой программы нет!🤷")
        show_main_instructions()  # показываем инструкции после ошибки
