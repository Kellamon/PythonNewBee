a = 'hello'
for i in a:
    print(i, end = ' ') # выведется hello, но построчно

#начало диапазона     шаг    
for e in range(2, 10, 2):
    print(e) # выведется от 0 до 9 элемнтов(в сумме 10))
    
for ind in range(len(a)): # вместо hello -> 0, 1, 2, 3 , 4
    print(a[ind]) 
    
    
for _ in range(3): # использование цикла для повторения ( _ - означает не важность переменных )
    print('Hello')