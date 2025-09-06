#functions
import math
import random
import os
import time
import socket
import subprocess
import platform
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


def random_number():
    print("Генератор случайных чисел")
    exit_code = "0"

    while True:
        user_input = input("Введите диапазон (например: 1-100) или 0 для выхода: ")

        if user_input == exit_code:
            break

        if '-' in user_input:
            start, end = map(int, user_input.split('-'))
            result = random.randint(start, end)
            print(f"Случайное число: {result}")
        else:
            print("Неверный формат! Используйте: начало-конец")

    return

def torque_calculator():
    print("Калькулятор крутящего момента (Введите 0 для выхода) ")
    z = (0)  # знак для выхода

    while True:
        print(
            "\nКрутящий момент будет рассчитываться по Лошадиным силам (мощность), оборотам двигателя и передаточному числу + редуктор\n")

        # Ввод мощности
        hp = float(input("Введите мощность двигателя в лошадиных силах: "))
        if hp == z:
            break
        kw = hp * 0.7355  # перевод в кВт

        # Обороты для расчёта
        n_values = [1000, 2000, 3000, 4000, 5000, 6000]

        # Ввод передаточных чисел
        gear1 = float(input("Введите передаточное число для 1 передачи (*ваше число* : 1): "))
        if gear1 == z:
            break
        r = float(input("Введите передаточное число для редуктора (*ваше число* : 1): "))
        if r == z:
            break
        eta = float(input("Введите общее кпд для трансмиссии и редуктора (Для максимального реализма рекомендуется значение 0.93): "))
        if eta == z:
            break

        # Убывающий ряд передач (нормализованный относительно первой передачи)
        gear_multipliers = [1.0, 0.64, 0.43, 0.34, 0.26, 0.20, 0.16, 0.13]
        gear_values = [gear1 * m for m in gear_multipliers]

        print("\nРассчёт, подождите секундочку...\n")

        # Вывод по каждой передаче
        for i, g in enumerate(gear_values, start=1):
            print(f"\n{i} передача (gear = {g:.3f} : 1):")
            time.sleep(1)
            for n in n_values:
                # Момент на коленвале по формуле: M = P * 9550 / n
                torque_engine = (kw * 9550) / n
                # Момент на колёсах с учётом передачи, редуктора и КПД
                torque_wheel = torque_engine * g * r * eta
                if torque_wheel <= 5000:
                    print(f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м")
                    time.sleep(0.2)
                elif torque_wheel <= 8500:
                    print(
                        f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м \nПРОБУКСОВКА КОЛЕС! БОЛЬШОЙ МОМЕНТ!")
                    time.sleep(0.2)
                elif torque_wheel <= 10000:
                    print(
                        f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м \nПРОБУКСОВКА СЦЕПЛЕНИЯ! СЛИШОМ БОЛЬШОЙ МОМЕНТ!ЧЕРЕЗ ВРЕМЯ ПРИВОДИТ К ПОЛОМКАМ!")
                    time.sleep(0.2)
                elif torque_wheel <= 15000:
                    print(
                        f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м \nПОЛОМКА ШЕСТЕРНЕЙ КОРОБКИ ПЕРЕДАЧ! ВЫЖЕГАНИЕ СЦЕПЛЕНИЯ! СЛИШОМ БОЛЬШОЙ МОМЕНТ! ДВИЖЕНИЕ ЗАТРУДНЕНО!")
                    time.sleep(0.2)
                elif torque_wheel <= 20000:
                    print(
                        f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м \nМНГНОВЕННАЯ ПОЛОМКА КОРОБКИ ПЕРЕДАЧ! МНГНОВЕННАЯ ПОЛОМКА СЦЕПЛЕНИЯ! СЛИШОМ БОЛЬШОЙ МОМЕНТ! ДВИЖЕНИЕ НЕВОЗМОЖНО!")
                    time.sleep(0.2)
                elif torque_wheel >= 20000:
                    print(
                        f"{n} об/мин → момент на коленвале: {torque_engine:.2f} Н·м, на колёсах: {torque_wheel:.2f} Н·м \nВЗРЫВ КОРОБКИ ПЕРЕДАЧ! РАЗРЫВ КАРДАНОВ! ВЕРОЯТНЫ НЕПРЕДВИДЕННЫЕ УЧЕНЫМИ ПОЛОМКИ! НЕРЕАЛИСТИЧНО БОЛЬШОЙ МОМЕНТ! ДВИЖЕНИЕ НЕРЕАЛЬНО!")
                    time.sleep(0.2)
    else:
        return

def ip_check():
    import socket
    import subprocess
    import platform

    print("\nIP checker (Введите 0 для выхода) ")
    z = "0"  # знак для выхода
    start = input("Нажмите Enter для вывода информации о подключении ")
    while True:
        if start == z:
            break
        print()

        def get_local_ip():
            """Получаем локальный IP через сокеты"""
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))  # Google DNS
                local_ip = s.getsockname()[0]
                s.close()
                return local_ip
            except:
                return "Не удалось определить локальный IP"

        def get_ip_system_command():
            """Получаем IP через системные команды"""
            system = platform.system()
            try:
                if system == "Windows":
                    result = subprocess.run(['ipconfig'], capture_output=True, text=True, encoding='cp866')
                    output = result.stdout
                    lines = output.split('\n')
                    for line in lines:
                        if 'IPv4' in line or 'Адаптер' in line:
                            if ':' in line and '.' in line:
                                return line.split(':')[-1].strip()
                elif system in ["Linux", "Darwin"]:
                    result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
                    return result.stdout.strip()
                return "Не удалось определить IP через команду"
            except Exception as e:
                return f"Ошибка выполнения команды: {e}"

        def get_network_info_complete():
            """Собираем полную информацию о сети"""
            hostname = socket.gethostname()
            local_ip = get_local_ip()
            system_ip = get_ip_system_command()
            return {
                'hostname': hostname,
                'local_ip_socket': local_ip,
                'system_ip_command': system_ip,
                'platform': platform.platform(),
                'system': platform.system()
            }

        # **Прямой вызов функций**
        print("=" * 60)
        print("ПОЛУЧЕНИЕ IP АДРЕСА")
        print("=" * 60)

        info = get_network_info_complete()

        print(f"Операционная система: {info['system']}")
        print(f"Платформа: {info['platform']}")
        print(f"Имя компьютера: {info['hostname']}")
        print(f"Локальный IP (wifi): {info['local_ip_socket']}")
        print(f"IP из системной команды: {info['system_ip_command']}")

        print("=" * 60)
        final = input("Для повторной проверки нажмите Enter или 0 для выхода: ")
        if final == z:
            break
    else:
        return
