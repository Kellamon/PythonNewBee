def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot] # используем срез списков[1:]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)  # pivot перевели в список [pivot] что бы не было ошибки по сравнению чисел
print(quick_sort([10, 5, 2]))