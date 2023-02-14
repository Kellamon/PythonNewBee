# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input("Введите число А: "))
B = int(input("Введите число В: "))
def exponentiation(A):
    if A > 0:
        return A ** B
    return 0
print(exponentiation(A))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

a, b = map(int, input('Введите число "a" и "b" через пробел: ').split())

def sum(a, b):
    a += 1
    b -= 1
    if  b > 0:
        return sum(a, b)
    else:
        return a - 1
Answer = sum(a, b)
print(Answer)