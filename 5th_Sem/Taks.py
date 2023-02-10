# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fibonacci(num):
#     if num == 0:
#         fib = 0
#     elif num == 1:
#         fib = 1
#     else:
#         fib = fibonacci(num - 1) + fibonacci(num - 2)
#     return fib
# n = int(input('Введите искомое значение: '))
# for i in range(n):
#     print(fibonacci(i))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# lst = []
# n = int(input('Введите количество оценок: '))
# min_mark = 5
# max_mark = 0
# lst = [int(input(f'Введите оценку: ')) for i in range(n)]
# for i in lst:
#     if min_mark > i:
#         min_mark = i
#     if i > max_mark:
#         max_mark = i
# print(lst)
# for i in range(len(lst)):
#     if lst[i] == min_mark:
#         lst[i] = max_mark
# print(lst)

#Напишите функцию, которая приниммает одно число и проверяет, 
# является ли оно простым

# def searchnumbers(n):
#     for i in range(2, n):
#         if(n % i == 0):
#             return 'не простое'
#         return 'простое'
# print(searchnumbers(23))

