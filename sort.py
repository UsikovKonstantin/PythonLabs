import random


# Returns a list of n elements with integers in the range [mn, mx].
def generate_list(n: int, mn: int, mx: int):
    lst = []
    for i in range(0, n):
        lst.append(random.randint(mn, mx))
    return lst


# Sorts the list, if reverse is true then sorts in reverse order.
def quick_sort(lst, reverse=False):
    quick_sort_range(lst, 0, len(lst) - 1)
    if reverse:
        lst.reverse()


# Recursive quick sort method.
def quick_sort_range(lst, left, right):
    if left >= right:
        return
    i = left
    j = right
    mid = lst[random.randint(left, right)]
    while i <= j:
        while lst[i] < mid:
            i += 1
        while lst[j] > mid:
            j -= 1
        if i <= j:
            (lst[i], lst[j]) = (lst[j], lst[i])
            i += 1
            j -= 1
        quick_sort_range(lst, left, j)
        quick_sort_range(lst, i, right)
