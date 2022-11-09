def summa(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


def recurs_count(arr):
    if arr == []:
        return 0
    return 1 + recurs_count(arr[1:])


def max_number(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


def max_number_rec(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_number_rec(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def quicksort(array):
    if len(array) < 2:
        return array  # base
    else:
        pivot = array[0]  # recurs
        less = [i for i in array[1:] if i < pivot]  # arr less then pivot
        greater = [i for i in array[1:] if i > pivot]  # arr more then pivot
        return quicksort(less) + [pivot] + quicksort(greater)


# print(summa([1, 2, 3]))
# print(recurs_count([1, 2, 3]))
# print(max_number([1, 2, 3, 4, 11]))
print(max_number_rec([1, 2, 3, 4, 11]))
# print(quicksort([]))
print(quicksort([11, 3, 5, 2, 6]))
