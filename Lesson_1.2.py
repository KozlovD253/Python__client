"""Каждое из слов «class», «function», «method» записать в байтовом типе
 без преобразования в последовательность кодов (не используя методы encode и decode)
 и определить тип, содержимое и длину соответствующих переменных."""

words = [b'class', b'function', b'method']

for i in words:
    print('word:{}'.format(i))
    print('type:{}'.format(type(i)))
    print('length:{}'.format(len(i)))

