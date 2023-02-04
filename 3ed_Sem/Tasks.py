# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.


numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(len(unique_numbers))

# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.

list_1 = [5, 4, 6, 7, 8, -10]
k = 3

list_result = list()
for i in range(k):
    list_result.append(list_1[len(list_1) - 1 - i])
    print(list_result)
print(1)
for i in range(len(list_1) - k):
    list_result.append(list_1[i])
    print(list_result)
print(list_result)

# Напишите программу для печати всех уникальных значений в словаре. 
# list_1 = [{"V": "S001"}, {"V": "S002"}, 
# {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
# {" V ":" S009 "}, {" VIII ":" S007 "}]
 
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set_1 = set()
for i in list_1:
    print(i)
    for j in i:
        print(j)
        set_1.add(i[j])
print(set_1)


# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером). 
# list_1 = [0, -1, 5, 2, 3]

array = [0, -1, 5, 2, 3]
i = 1
n = 0
for i in range(1, len(array)):
    if array[i] > array[i-1]:
        n += 1
print(n)