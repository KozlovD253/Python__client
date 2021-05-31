"""Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for i in words:
    l = i.encode('utf-8')
    print(f'в байтовом виде: {l, type(l)}')
    m = bytes.decode(l, 'utf-8')
    print(f'в строковом: {m, type(m)}')
