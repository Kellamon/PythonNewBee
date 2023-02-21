# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
#            не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
#            что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
#            Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
#            Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
#            В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#      Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
#      Вывод: Парам пам-пам

# vinnies_flow = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
vinnies_flow = 'Если-я-чешу-в-затылке,-не-беда. В-голове-моей-опилки.-ДА-да-ДА!'
print(vinnies_flow.split())
vowels = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё', 'e', 'u', 'i', 'o', 'a', 'y'}


def count_syllables(text):
    amount = 0
    for char in text:
        if char.lower() in vowels:
            amount += 1
    return amount


def chek_the_rithm(flow):
    for line in range(len(flow)):
        if count_syllables(flow[line]) != count_syllables(flow[0]):
            return 'Пам парам'
    return 'Парам пам-пам'


# temp = list(map(count_syllables, vinnies_flow.split()))
# print(temp)
print(chek_the_rithm(vinnies_flow.split()))

print()

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
#           аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
#           указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет
#           с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
#           ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()


print_operation_table(lambda x, y: x * y)