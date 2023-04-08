import random

maximum_threshold = 10  # уровень сложности по умолчанию, максимальное число
GAME_MENU = """Тренажёр счёта Account Simulator
    1 - Начать игру.
    2 - Рекорды.
    3 - Настройки.
    4 - Выход"""
RULE_GAMES = """Вам будут задавать вопросы, и вы должны на них отвечать, 
ваша задача - набрать наибольшее количество балов."""

operation_calc = "+"


def calculate(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    else:
        return "НЕТ ТАКОЙ ОПЕРАЦИИ"


while True:
    points = 0
    print(GAME_MENU)
    user_choice = input("Введите суда свой выбор (цифра).")
    if user_choice == "1":
        print(RULE_GAMES)
        print("Введите своё имя")
        name = input()
        print("Добро пожаловать,", name, "!", sep="")
        while True:
            first_select_random = random.randint(1, maximum_threshold)
            second_random_selection = random.randint(1, maximum_threshold)
            result = calculate(number1=first_select_random, number2=second_random_selection, operation=operation_calc)
            print(first_select_random, operation_calc, second_random_selection, "=?", sep="")
            user_response = int(input("Введите свой ответ"))
            if user_response == result:
                print("Верно! Следующий вопрос.")
                points = points + 10
                print("Сейчас у вас очков:", points, "!")
            else:
                print("Ошибка! Правильный ответ:", result, ",начни с начала")
                score_data = open(file="Score.txt")
                best_score = int(score_data.read())
                score_data.close()

                # Запоминать / обновлять лучший результат
                if best_score < points:
                    best_score = points
                    print("Лучший результат-", best_score, ".")
                    score_data = open(file="Score.txt", mode="w")
                    score_data.write(str(best_score))
                    score_data.close()
                break
    elif user_choice == "2":
        score_data = open(file="Score.txt")
        best_score = score_data.read()
        score_data.close()
        print("На данный момент ваш лучший результат:", best_score, "!", sep="")
    elif user_choice == "3":

        user_choice = input("""
        1 - Выбрать сложность
        2 - Выбрать операцию""")

        if user_choice == "1":
            DIFFICULTY_SELECTION = """Выберите сложность:
            1 - Базовый.
            2 - Не простой.
            3 - Сложный.
            4 - EXPERT"""
            print(DIFFICULTY_SELECTION)
            user_difficulty_selection = input("Введите суда свой выбор (цифра).")
            if user_difficulty_selection == "1":
                maximum_threshold = 11
                print("Вы оставили базовый уровень сложности")
            elif user_difficulty_selection == "2":
                maximum_threshold = 101
                print("Вы выбрали не простой путь")
            elif user_difficulty_selection == "3":
                maximum_threshold = 501
                print("Вы выбрали сложный уровень")
            elif user_difficulty_selection == "4":
                maximum_threshold = 1001
                print("Теперь вы EXPERT")
            else:
                print("Вы ввели неправильное значение")
        elif user_choice == "2":
            user_choice = input(""" Выберите операцию
                   1 - Умножение
                   2 - Деление """)

            if user_choice == '1':
                operation_calc = "*"

    elif user_choice == "4":
        break
    else:
        print("Нет такого выбора!")
