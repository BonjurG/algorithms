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


# print(summa([1, 2, 3]))
# print(recurs_count([1, 2, 3]))
#print(max_number([1, 2, 3, 4, 11]))
print(max_number_rec([1, 2, 3, 4, 11]))
