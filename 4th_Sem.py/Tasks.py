# Напишите программу, которая принимает на вход строку, отслеживает, 
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n

string = 'd g h t r g r h t j h b v f d s d f'
print(string)
my_list = string.split()
my_dict = {}
new_list = []
for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1   # используем метод гет по ключу letter
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)
print(' '.join(new_list))


# # Пользователь вводит текст(строк).
# # Словом считается последовательность непробельных символов идущих подряд,
# # слова разделены одним или большим числом пробелов.
# # Определите, сколько различных слов содержится в этом тексте.

string = 'sdsd sdsd sdsdf   fsdfg ggk    lgg lkjlkl sdsd'
my_list = string.split(' ') # если убрать пробел тут, то строчки с ремув не нужны
print(my_list)
my_dict = set(my_list)
print(my_dict)
my_dict.remove('') # убрали пробелы в строке
print(my_dict)
print(f'В нашем тексте {len(my_dict)} уникальных слов(а)')

# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательнсоти
# Пример
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

num = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
my_dict = {}

for n in num:
    my_dict[n] = my_dict.get(n, 0) + 1
    
for i in my_dict:
    if my_dict.get(i) == 1:
        new_list.append(i)
        
print(new_list)