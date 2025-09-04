import random
import os
import math


def coin_flip():
    print("Программа подбрасывания монетки")
    z = "0"  # знак для выхода

    while True:
        x = input("Нажми Enter чтобы подбросить монетку, или 0 чтобы выйти: ")

        if x == z:
            break

        # основной код
        result = random.choice(["Орёл", "Решка"])
        print("Выпало:", result)

    else:
        return

def Checking_a_prime_number():
    print("Проверка на простое число. Для выхода введите 0")
    z = (0)  # знак для выхода

    while True:

        i = int(input("Введи число для проверки: "))
        if i == z:
            break
        flag = True
        divisors = []

        if i == 1:
            print("Не простое число")
        else:
            for s in range(2, int(math.sqrt(i)) + 1):
                if i % s == 0:
                    flag = False
                    divisors.append(s)
                    divisors.append(i // s)

            if flag:
                print("Простое")
            else:
                print("Не простое число")
                divisors = sorted(set(divisors))
                print("Делится на:", divisors)
    else:
        return


def LCM_GCD():
    print("Калькулятор НОК И НОД (для выхода введите 0)")
    z = "0"  # знак для выхода

    while True:

        # основной код
        while True:
            def is_prime(num):
                if num < 2:
                    return False
                for s in range(2, int(math.sqrt(num)) + 1):
                    if num % s == 0:
                        return False
                return True
            print("Работа с 6+ значными числами может обрабатоваться дольше обычного!")
            A = int(input("Введи первое число: "))
            B = int(input("Введи второе число: "))
            print("\n Секундочку...\n")

            pn = [n for n in range(2, max(A, B)+1) if is_prime(n)]
            N = len(pn)  # количество простых чисел в списке

            nA = A
            nB = B
            i = -1
            sA = [0] * N
            sB = [0] * N
            for M in pn:
                i = i + 1
                while A % M == 0:
                    sA[i] += 1
                    A //= M
                while B % M == 0:
                    sB[i] += 1
                    B //= M

            # НОД и НОК
            NOD = 1
            NOK = 1
            for i, M in enumerate(pn):
                NOD *= M ** min(sA[i], sB[i])
                NOK *= M ** max(sA[i], sB[i])

            print("НОД числа ", nA, "и числа ", nB, " равен = ", NOD)
            print("НОК числа ", nA, "и числа ", nB, " равен = ", NOK)

            e = input("Для выхода нажми 0, а для продолжения нажми Enter ")
            if e == z:
                 break
        if e == z:
            break



def text_to_binary():
    print("Текст в двоичный код (для выхода введите 0)")
    z = "0"  # знак для выхода

    while True:
        x = input("Введи текст для превращения в двоичный код: ")

        if x == z:
            break

        # основной код
        binary_result = " ".join(format(ord(char), "08b") for char in x)
        print("Двоичный код:", binary_result)

    else:
        return

def BMI():
    print("Калькулятор ИМТ (для выхода введите 0)")
    z = 0  # знак для выхода

    while True:

        # основной код
        h = float(input("Напиши свой рост в сантиметрах: "))
        if h == z:
            break
        w = float(input("Напиши свой вес в КГ: "))
        if w == z:
            break
        print("Расчет...")
        bmi = int(10000 * w / (h * h))
        print("Твой индекс массы тела:", bmi)
        if bmi <= 18:
            print("Недостаток веса")
        elif 18 < bmi <= 30:
            print("Нормальный вес")
        else:
            print("Выше нормы")
        if bmi == 0:
            print("ОШИБКА, ПОПРОБУЙ ЕЩЕ")
    else:
        return

def shutdown_timer():
    print("Таймер для выключения устройства")
    z = "0"  # знак для выхода

    while True:
    #код
        minutes = float(input("Через какое количество времени вы хотите выключить ваше устройство? Напишите в минутах (не меньше минуты): "))
        seconds = minutes * 60
        print("Ваше устройство выключиться через", minutes, "минут, или через", seconds, "секунд")
        os.system(f"shutdown /s /t {seconds}")
    else:
        return

def generate_password():
    print("Генератор случайного пароля (для выхода введите 0)")
    z = (0)  # знак для выхода

    # создаём строки символов вручную
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    chars = letters + digits + punctuation

    while True:
        o = int(input("Сколько символов вы хотите в пароле? (Введи 0 для выхода) "))
        if o == z:
            break
        x = input("\nНажми Enter чтобы сгенерировать пароль или 0 чтобы выйти: ")
        if x == z:
            break
        password = "".join(random.choice(chars) for _ in range(o))
        print("Сгенерированный пароль:", password)
    else:
        return

def check_password():
    print("Проверка безопасности пароля (для выхода введите 0)")
    z = "0"  # знак для выхода

    letters_lower = "abcdefghijklmnopqrstuvwxyz"
    letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    while True:
        password = input("Введите пароль для проверки или 0 для выхода: ")
        if password == z:
            break

        has_lower = any(c in letters_lower for c in password)
        has_upper = any(c in letters_upper for c in password)
        has_digit = any(c in digits for c in password)
        has_punct = any(c in punctuation for c in password)
        length_ok = len(password) >= 8
        length_bonus = len(password) >= 12

        score = 0
        score += 2 if length_ok else 0
        score += 2 if has_lower else 0
        score += 2 if has_upper else 0
        score += 2 if has_digit else 0
        score += 2 if has_punct else 0
        if length_bonus:
            score += 2

        if score >= 10:
            print(f"Пароль СУПЕР надежный ✅ (Оценка: {score}/10)")
        elif score == 10:
            print(f"Пароль очень надёжный ✅ (Оценка: {score}/10)")
        elif score >= 7:
            print(f"Пароль надёжный 👍 (Оценка: {score}/10)")
        else:
            print(f"Пароль слабый ❌ (Оценка: {score}/10)")

        print("Требования для надёжного пароля:")
        if not length_ok:
            print("- Длина минимум 8 символов")
        if not has_lower:
            print("- Наличие строчных букв")
        if not has_upper:
            print("- Наличие заглавных букв")
        if not has_digit:
            print("- Наличие цифр")
        if not has_punct:
            print("- Наличие специальных символов")
    else:
        return

def generate_login():
    print("Генератор логина (для выхода введите 0)")
    z = "0"  # знак для выхода

    # набор случайных слов (можно расширить)
    words = ["Сat", "Dog", "Sun", "Moon", "Star", "Tree", "Book", "Sky", "Rain", "Fire"]

    while True:
        x = input("Нажми Enter для продолжения или 0 чтобы выйти: ")
        if x == z:
            break

        # выбор количества слов
        num_words = input("Сколько слов в логине? (например, 2): ")
        if not num_words.isdigit():
            print("Введите число!")
            continue
        num_words = int(num_words)

        # нужно ли добавлять цифры
        add_numbers = input("Добавлять цифры в конец логина? (да/нет): ").lower()
        add_numbers = add_numbers.startswith("д")  # True если 'да'

        # выбираем случайные слова
        chosen_words = [random.choice(words) for _ in range(num_words)]
        login = "".join(chosen_words)

        # добавляем цифры после букв, если нужно
        if add_numbers:
            digits = "0123456789"
            num_digits = random.randint(4, 8)  # случайное количество цифр
            login += "".join(random.choice(digits) for _ in range(num_digits))

        print("\nСгенерированный логин:", login)
    else:
        return
