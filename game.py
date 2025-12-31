import random

# Загаданное слово
word = "программирование"
guessed_letters = set()
score = 0
hints = 2

# Выбор уровня сложности
print("Выберите уровень сложности:")
print("1 — Лёгкий (10 попыток)")
print("2 — Средний (7 попыток)")
print("3 — Сложный (5 попыток)")

level = input("Введите номер уровня: ")

if level == "1":
    attempts = 10
elif level == "2":
    attempts = 7
else:
    attempts = 5

# Основной игровой цикл
while attempts > 0:
    # Отображение текущего состояния слова
    current_word = ""
    for letter in word:
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += "_"

    print("\nСлово:", current_word)
    print("Оставшиеся попытки:", attempts)
    print("Подсказки:", hints)
    print("Счёт:", score)

    # Проверка победы
    if "_" not in current_word:
        print("\nПоздравляем! Вы угадали слово!")
        print("Итоговый счёт:", score)
        break

    user_input = input("Введите букву или слово 'подсказка': ").lower()

    # Подсказка
    if user_input == "подсказка":
        if hints > 0:
            unopened_letters = [l for l in word if l not in guessed_letters]
            hint_letter = random.choice(unopened_letters)
            guessed_letters.add(hint_letter)
            hints -= 1
            print(f"Подсказка: открыта буква '{hint_letter}'")
        else:
            print("Подсказки закончились")
        continue

    # Проверка ввода
    if len(user_input) != 1:
        print("Введите одну букву")
        continue

    # Проверка буквы
    if user_input in guessed_letters:
        print("Эта буква уже была введена")
    elif user_input in word:
        guessed_letters.add(user_input)
        score += 1
        print("Верно!")
    else:
        attempts -= 1
        print("Неверно!")

# Поражение
if attempts == 0:
    print("\nВы проиграли.")
    print("Загаданное слово:", word)
