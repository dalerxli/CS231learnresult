"""
cs231
create by swm
2018/02/07
"""


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr)/2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print(quicksort([3, 4, 5, 1, 54, 76, 7, 53, 6]))