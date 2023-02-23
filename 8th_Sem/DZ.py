# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines.(на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:

def read_last(enter_file: str = 'article.txt', use_lines: int = 0):
        with open(f'{enter_file}', 'r', encoding="utf-8") as use_file:
            data_list = use_file.readlines()

        if 0 <= use_lines <= len(data_list):
            for i in range(1, use_lines + 1):
                print(data_list[-i], end="")
        else:
            print("Что то пошло не так, может введенное значение меньше '0'?")
    
lines = int(input('Введиете кол-во строк: '))
file = input('Введите название файла (article.txt): ')
read_last(use_lines=lines, enter_file=file)

