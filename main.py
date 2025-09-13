import random


def draw_hangman(attempts):
    """Рисует виселицу в зависимости от количества попыток"""
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        """,
        """
           ------
           |    |
           |    O1111111111111111111111111
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           | game over 
           |    tttttttt
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |   
           |   
           |
        """
    ]
    return stages[attempts]


def hangman():
    """Основная функция игры"""
    # Список слов для угадывания
    words = ['питон', 'программа', 'компьютер', 'алгоритм', 'библиотека',
             'программист', 'виселица', 'клавиатура', 'мышка', 'монитор']

    # Выбираем случайное слово
    secret_word = random.choice(words)
    guessed_letters = []  # Угаданные буквы
    attempts = 6  # Количество попыток

    print("Добро пожаловать в игру 'Виселица'!")
    print("Я загадал слово. Попробуй угадать его по буквам.")
    print(f"У тебя есть {attempts} попыток.")

    while attempts > 0:
        # Показываем текущее состояние слова
        display_word = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '

        print(f"\nСлово: {display_word}")
        print(f"Осталось попыток: {attempts}")
        print(f"Использованные буквы: {', '.join(guessed_letters)}")

        # Рисуем виселицу
        print(draw_hangman(attempts))

        # Получаем букву от игрока
        guess = input("Введите букву: ").lower()

        # Проверяем ввод
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже пробовали эту букву!")
            continue

        guessed_letters.append(guess)

        # Проверяем, есть ли буква в слове
        if guess in secret_word:
            print("Правильно! Эта буква есть в слове.")
        else:
            print("К сожалению, этой буквы нет в слове.")
            attempts -= 1

        # Проверяем, выиграл ли игрок
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nПоздравляю! Ты угадал слово: {secret_word}")
            break
    else:
        # Если закончились попытки
        print(draw_hangman(0))
        print(f"\nТы проиграл! Загаданное слово было: {secret_word}")

    # Предлагаем сыграть еще раз
    play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        hangman()
    else:
        print("Спасибо за игру!")


# Запускаем игру
if __name__ == "__main__":
    hangman()