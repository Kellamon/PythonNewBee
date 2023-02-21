#with open('les8test.txt', 'r', encoding='utf-8') as file:   # r - чтение, w - запись, a - добавление в файл
    # text = file.read().splitlines()  #text = file.readlines() позволяет добавить \n с указанием на отступ новой строки    
    # print(text)
    # # используем для постоянной работы с файлом. Если этого нам не нужно, используем нижеприведенный способ для кратковременного использования данных
    
    # while True:
    #     line = file.readline()
    #     if not line:    
    #         break
    #     print(line.strip())  # strip позволяет устранить сырые символы типа пробела и т.д.
        
# with open('filetest.txt', 'w', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')       

# поиск буквы в тексте и ее подсчет.
with open('filetest.txt', 'r', encoding='utf-8') as file: 
    text = file.read() 
    print(text.count(input()))
    
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# 9 8 7 6 5 6 7 8 9

# from random import randint
# with open('les8test.txt', 'w') as file:
#     for _ in range(10):
#         file.write(str(randint(0, 9)) + '\n')
#         spis = []
#         for _ in range(10):
#             spis.append(randint(1, 10))
#                 multi = 1
# with open('les8test.txt', 'r') as file:
#     for el in file.read().split():
#         multi *= spis[int(el)]
#         print(spis[int(el)])
#         print(multi)

from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('les8test.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('les8test.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)


