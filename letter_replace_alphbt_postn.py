"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""

# Пользовательский ввод английского текста
given_str = input('Enter some english text:')

# Функция для конвертации пользовательского ввода в список состоящий только из букв [a-z & A-Z]
def convert_str_list(str1):
    lst = [x for x in str1 if 97 <= int(ord(x)) <= 122 or 65 <= int(ord(x)) <= 90]
    return list(map(lambda x: x.lower(), lst))

conv_list = convert_str_list(given_str)

# Здесь создаю словарь  "буква англ. алфавита : числовое значение позиции буквы в англ. алфавите
alph = []
alph[:0] = list('abcdefghijklmnopqrstuvwxyz')
i = 0
alph_dict = {}
for x in alph:
   i += 1
   alph_dict.update({x: i})

# Шифрую пользовательский текст цифрами обозначающими числовое значение позиции буквы в англ. алфавите
lst = []
for i in conv_list:
    for key, value in alph_dict.items():
        if i == key:
            lst.append(value)

# Превращаю конечный список в стринг
mystring = ' '.join(map(str,lst))

print(mystring)
