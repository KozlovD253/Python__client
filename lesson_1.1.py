"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые
представление в формат Unicode и также проверить тип и содержимое переменных.и"""

word_1 = 'разработка'
word_1_bytes = word_1.encode('utf-8')
print(word_1_bytes)
print(type(word_1), type(word_1_bytes))
print('*' * 15)
word_2 = 'сокет'
word_2_bytes = word_2.encode('utf-8')
print(word_2_bytes)
print(type(word_2), type(word_2_bytes))
print('*' * 15)
word_3 = 'декоратор'
word_3_bytes = word_3.encode('utf-8')
print(word_3_bytes)
print(type(word_3), type(word_3_bytes))

