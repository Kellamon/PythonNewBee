import os

# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines.(на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(enter_file: str = 'article.txt', use_lines: int = 0):
        with open(f'{enter_file}', 'r', encoding="utf-8") as use_file:
            data_list = use_file.readlines()

        if 0 <= use_lines <= len(data_list):
            for i in range(1, use_lines + 1):
                print(data_list[-i], end=" " + '\n')
        else:
            print("Что то пошло не так, может введенное значение меньше '0'?")
    
lines = int(input('Введиете кол-во строк: '))
file = input('Введите название файла (article.txt): ')
read_last(use_lines=lines, enter_file=file)

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), 
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, "r", encoding='utf-8') as text:
        words = text.read().split()
 
    max_length = len(max(words, key=len))
    sought_words = [word for word in words if len(word) == max_length]
 
    f = "result.txt"
    i = 1
    while os.path.exists(f):
        f = f"result{i}.txt"
        i += 1
    with open(f, 'w', encoding='utf-8') as file:
        file.write(' '.join(sought_words) + "\n")
 
 
longest_words('article.txt')

# # Вариант без вывода списка слов
# def longest_words(file):
#     with open(file, "r", encoding='utf-8') as text:
#         words = text.read().split()
 
#     max_length = max(words, key=lambda i: len(i))
#     print(max_length)
 
 
# longest_words('article.txt')