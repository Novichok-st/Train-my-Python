import random


def randomArray():
    words = "aAbBcCdDeEfFgGhHiIjJkKlLmMoOpPqQrRsStTuUvVwWxXyYzZ"
    items = []
    for i in range(random.randint(1, 10)):
        items.extend(str(random.randint(1, 100)))

    for i in range(random.randint(1, 10)):
        items.extend(random.choice(words))

    print(items)


# JavaScript в python
class console:
    def log(*args):
        print(*args)


# камень ,ножницы, бумага
class KamenNojnicciBymaga:
    def game():
        runner = True
        # цикл работает пока не написать quit
        while runner:
            # выборы ИИ
            choises = ["камень", "ножницы", "бумага"]
            # игрок
            player = input("Камень Ножницы Бумага ??? → ").lower()
            # ИИ
            ai = random.choice(choises)
            # Варианты выборов
            if player == "камень" and ai == "бумага":
                print(f"Проигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")
            elif player == "бумага" and ai == "камень":
                print(f"Выигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")

            elif player == "камень" and ai == "ножницы":
                print(f"Выигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")
            elif player == "ножницы" and ai == "камень":
                print(f"Проигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")

            elif player == "ножницы" and ai == "бумага":
                print(f"Выигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")
            elif player == "бумага" and ai == "ножницы":
                print(f"Проигрыш, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")
            elif player == ai:
                print(f"Ничья, {ai}")
                print("Хотите продолжить: Да→1;Нет→quit/2")

            if player in ["quit", "2"]:
                runner = False
