"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

words = ['attribute', 'класс', 'функция', 'type']

def not_ascii (word):
    try:
        bytes(word, 'ASCII')
    except UnicodeError:
        print(f'слова "{word}" не возможно записать в байтовом типе')

for word in words:
    not_ascii(word)