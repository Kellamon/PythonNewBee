import random

# 39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

array = []
N = int(input('Input N: '))
array_1 = []
M = int(input('Input M: '))
for i in range(N):
    array.append(int(input('Введите элементы в массиве N: ')))
print(array)

for i in range(M):
    array_1.append(int(input('Введите элементы в массиве M: ')))
print(array_1)
array_2 = []

for i in array:
    if array_1.count(i) < 1:
        array_2.append(i)
print(array_2)

# Вариант решения от преподавателя

# 1й

first_list = [int(input()) for _ in range(int(input('Введите количество элементов: ')))]
second_list = [int(input()) for _ in range(int(input('Введите количество элементов: ')))]
for el in first_list:
    if el not in second_list:
        print(f'элемент массива "N" {el} ')

# 2й

first_list = [random.randint(1, 100) for _ in range(10 ** 6)]
second_list = [random.randint(1, 100) for _ in range(10 ** 6)]
second_set = set(second_list)
for el in first_list:
    if el not in second_set:
        print(f'элемент массива "N" {el} ')

# 41. Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

array = [1, 2, 3, 4, 7]
print(array)
for i in range(2, len(array) - 1):
    count = 0
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1
print(count)


# Вариант решения от преподавателя
some_list = [int(input()) for _ in range(int(input('Введите кол-во чисел: ')))]
count = 0
for ind in range(1, len(some_list) - 1):
    if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
        count += 1
print(count)



# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

array = [1, 2, 3, 4, 7, 5, 3, 6, 1, 6, 4]
array_1 = []
count = 0
for i in array:
    if array.count(i) > 1 and i not in array_1:
        count += 1        
        array_1.append(i)
print(array)
print(array_1)
print(count)


# Вариант решения от преподавателя

some_list = []
while True:
    number = int(input('Ввод чисел: '))
    if number == 0:
        break
    some_list.append(number)
    
count_dict = {} #2: 2, 3: 3, 4: 1, 5: 1 создает ключи для поиска

for el in some_list:
    if count_dict.get(el):
        count_dict[el] += 1
    else:
        count_dict[el] = 1
print(count_dict)

count = 0
for value in count_dict.values():
    count += value // 2
print(count)


# 45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10 ** 5. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def sum_div(n):
    summa = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            summa += i
    return summa

summ_dict = {}

k = int(input('Введите диапазон: '))
for number in range(1, k +1):
    if number in summ_dict:
        if sum_div(number) == summ_dict[number]:
            print(number, summ_dict[number])
    summ_dict[sum_div(number)] = number
    