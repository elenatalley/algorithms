# sort low to high, find smallest element of tuple

def find_smallest(arr):
    # для хранения наименьшего значения
    smallest = arr[0]
    # для хранения ИНДЕКСА наименьшего значения
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#  на основе этой фнук пишем фун сортиировки выбором

def selection_sort(arr):
    newArr = []
    for i in range (len(arr)):
        # находит наименьший элемент в массиве
        smallest = find_smallest(arr)
# добавляет его в новый массив
        newArr.append(arr.pop(smallest))
        return newArr

print(selection_sort([5,2,6,1,34,1,11,45]))

