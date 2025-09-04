import random


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
