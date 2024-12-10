#todo: Реализовать в игре "Поле чудес" возможность сохранять состояние игры (save game).
# Пользователю должна быть предоставлена возможность восстановиться из файла сериализации.
import pickle
import os
from random import randint as ri


words = None
desc_ = None
attempt = 0
word_for_play = ""
player_word = []

def init():
    global words, desc_
    words = ["operator", "constract", "object"]
    desc_ = [
        "Это слово обозначает наимнейшую автономную часть языка программирования.",
        "Это синтаксическая структура, которая определяет способ организации кода.",
        "Это сущность, представляющая собой экземпляр класса."
    ]
    global attempt
    attempt = 0

def get_attempt():
    return attempt

def set_attempt():
    global attempt
    attempt += 1

def get_word():
    global words
    word_index = ri(0, len(words) - 1)
    print_(word_index)
    return words[word_index]

def print_(word_index):
    global desc_
    print("Угадайте слово по подсказке: " + desc_[word_index] + "\n")

def get_field(word_for_play):
    return [" ▒"] * len(word_for_play)

def get_letter():
    letter = input(f"\nУ вас осталось {10 - get_attempt()} попыток! \nВведите букву (или 'save' для сохранения): ")
    return letter.lower()

def save_game(filename):
    with open(filename, "wb") as f:
        data = {
            'attempt': attempt,
            'word_for_play': word_for_play,
            'player_word': player_word
        }
        pickle.dump(data, f)
        print("Игра сохранена!")

def load_game(filename):
    global attempt, word_for_play, player_word
    with open(filename, "rb") as f:
        data = pickle.load(f)
        attempt = data['attempt']
        word_for_play = data['word_for_play']
        player_word = data['player_word']
        print("Игра загружена!")

def run():
    global word_for_play, player_word
    word_for_play = get_word()
    player_word = get_field(word_for_play)
    print("".join(player_word))
    engine(word_for_play, player_word)

def engine(word_for_play, player_word):
    global attempt
    max_attempts = 10
    while attempt < max_attempts:
        letter = get_letter()

        if letter == "save":
            filename = input("Введите имя файла для сохранения: ")
            save_game(f'./savegame/{filename}.pkl')
            continue  # Пропустить увеличение попыток

        if letter in word_for_play:
            for i, char in enumerate(word_for_play):
                if char == letter:
                    player_word[i] = letter
            print(" ".join(player_word))
        else:
            print(f"Буквы {letter} нет в слове.")
            set_attempt()

        if " ▒" not in player_word:
            print("Вы угадали слово! Поздравляем!")
            return

    print("У вас закончились попытки. Игра окончена!")


print('''
*******************************
********* ПОЛЕ ЧУДЕС **********

1. Начать игру !
2. Загрузить игру
0. Сохранить игру

''')

key = int(input('Ваш выбор % '))

match key:
    case 1:
        init()
        run()
    case 2:
        init()
        print("Доступные файлы для загрузки:")

        dir_ = os.listdir('./savegame')
        for file in dir_:
            print(file)
        name_save_game = input('Введите имя файла для загрузки: ')
        load_game(f'./savegame/{name_save_game}')
        print(f"Игра {name_save_game} загружена.")
        engine(word_for_play, player_word)
    case 0:
        name_save_game = input('Введите имя для сохранения: ')
        save_game(f'./savegame/{name_save_game}.pkl')


