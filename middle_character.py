"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

Вам дадут слово. Ваша задача — вернуть средний символ слова.
Если длина слова нечетная, вернуть средний символ.
Если длина слова четная, верните средние 2 символа.

Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
"""


given_word = input('Enter some english word:')

lst = []
lst[:0] = list(given_word)

if len(lst) % 2 == 0:
    mystring = ''.join(map(str, lst[len(lst)//2-1:len(lst)//2+1]))
    print(mystring)
else:
    print(''.join(map(str, lst[len(lst)//2])))