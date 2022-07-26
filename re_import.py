# import re
#
# s = 'Привет! Как дела? А у меня нормально.'
#
# result = re.findall(r'[бвгджзклмнпрстБВГДЖЗПК]\w+', s)
#
#
# someData = {
#     'car': 'Ford',
#     'model': 'mustang',
#     'year': 2015,
# }
#
# print(someData['car'])
#
# i = 1
#
# while i < 5:
#     print(i)
#     i += 1
#
#
# for x in range(1, 7):
#     print(x)
#
#
# def flipper(txt):
#     return 'flip' if txt == 'flop' else 'flop'
#
# flipper('flop')
#
# def print_numbers(n):
#     while n > 0:
#         print(n)
#         n -= 1
#     print('finished')
#
# print_numbers(4)
#
# --- ДВА РЕШЕНИЯ ОДНОЙ ЗАДАЧИ ---
#
# def print_reversed_word_by_symbol(name):
#     i = 1
#
#     while len(name) >= i:
#         print(name[-i])
#         i += 1
#
# def print_reversed_word_by_symbol(name):
#     b = list(name)
#     b.reverse()
#
#     for i in b:
#         print(i)
#
# print_reversed_word_by_symbol('123')
#
#
# ---- Функция подсчета символов в строке ----
# def count_chars(phrase, char):
#     char_lower = char.lower()
#     lower_phrase = phrase.lower()
#     chars_container = []
#     total = 0
#
#     for i in lower_phrase:
#         if i == char:
#             chars_container.append(i)
#
#     for i in chars_container:
#         total += 1
#
#     print(total) if total > 0 else print('no characters!!')
#
# count_chars('hello, KitTTyy', 'y')
#
#
# ----ВЫБОР СТРОКИ С УКАЗАННОГО МЕСТА----
# def selected_str(string, char):
#     i = 0
#     result = ''
#     try:
#         while i < int(char):
#             if char > len(str(string)):
#                 print('too many caracters!')
#                 break
#             result += string[i]
#             i+=1
#         return result
#     except TypeError: print('please, enter the string!')
#     finally: pass
#
# print(selected_str('sdfr', 3))
#
#
# ----ПРОВЕРКИ ПРЕДЫДУЩЕЙ ФУНКЦИИ----
# Вернуть False, если:
# Отрицательная длина извлекаемой подстроки.
# Отрицательный заданный индекс.
# Заданный индекс выходит за границу всей строки.
# Длина подстроки в сумме с заданным индексом выходит за границу всей строки.
# def is_arguments_for_substr_correct(str, start, length):
#     if start < 0: return False
#     elif length < 0: return False
#     elif start > len(str) - 1: return False
#     elif length + start > len(str): return False
#     else: return True
#
# print(is_arguments_for_substr_correct())
#
#
# ----Функция, удаляющая выбранный символ из строки (символ передается вторым аргументом)
# def filter_string(str, char):
#     filtered_str = ''
#
#     for symbol in str:
#         if symbol != char: filtered_str += symbol
#
#     return filtered_str
#
# print(filter_string('Hello', 'H'))
#
# ----Решение 2----
#
# sample = 'Hello'
# modified_sample = sample.replace('H', '')
#
# print(modified_sample)
#
#
# ----НАПИСАТЬ ПРОВЕРКУ НА НАЛИЧИЕ СИМВОЛА В СТРОКЕ ЧЕРЕЗ ЦИКЛ WHILE----
# функция принимает два аргумента: строку и символ
#
# def is_contains_char(text, char):
#
#     i = 0
#
#     while i < len(str(text)):
#         if text[i] == char:
#            return True
#         else: i += 1
#
#     return False
#
# print(is_contains_char('Hello', 'H'))
#
# ----ЗАДАНИЕ: функция переворачивает передаваемую СТРОКУ С ПОМОЩЬЮ ЦИКЛА for----
# Пример func('hello') ==> 'olleh':
# def x(txt):
#     reverse = ''
#
#     for i in txt:
#         reverse = i + reverse
#
#     print(reverse)
#
# x('hello')
#
#
# ----ЗАДАНИЕ: функция удаляет символ из строки с помощью цикла for. Функция нечувствительна к регистру
# пример вызова: filter_string('Hello', 'O') ==> Hell
# def filter_string(txt, char):
#     txt = txt.lower()
#     char = char.lower()
#     container = ''
#
#     for i in txt:
#         if i != char: container += i
#
#     if container == txt: return 'character not found.'
#
#     return container
#
# print(filter_string('hello, Zorro', 'O'))
#
#
# ---ЗАДАНИЕ: вывести в консоль фразу (с переносом строки, как в примере ниже)----
# - Did Joffrey agree?
# - He did. He also said "I love using \n".
#
# print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')
#
#


# НАПИСАТЬ ПРОГРАММУ, КОТОРАЯ ВЫВОДИТ РАНДОМНОЕ ЧИСЛО ОТ 1 ДО 10
# from random import random
#
# print(round(random()*10))

# Реализовать функцию, которая принимает массив цифр и выводит индексы этих цифр (ниже пример вывода)
# nums = [4, 5, 6]
# index_counter(nums) ==> number 4 has index 0 и тд...
#
#
# numbers = [1, 2, 3, 4]
#
# def index_counter(arr):
#     for i, num in enumerate(numbers): # Можно передать вторым аргументом стартовый индекс
#         print(f'number {num} has index {i}')
#
# index_counter(numbers)


