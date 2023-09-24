import random
import time


# Returns a list of n elements with integers in the range [mn, mx].
def generate_list(n: int, mn: int, mx: int):
    lst = []
    for i in range(0, n):
        lst.append(random.randint(mn, mx))
    return lst


# Generates a file 'file_name' with numbers.
def generate_file(lst, file_name: str):
    file = open(file_name, "w")
    file.write(str(len(lst)) + "\n")
    for item in lst:
        file.write(str(item) + "\n")
    file.close()


# Returns a list of numbers obtained from a file.
def get_list_from_file(file_name: str):
    file = open(file_name, "r")
    n = int(file.readline())
    lst = [0] * n
    for i in range(0, n):
        lst[i] = int(file.readline())
    return lst


# Writes the list to a file.
def write_list_to_file(lst, file_name: str):
    file = open(file_name, "w")
    for item in lst:
        file.write(str(item) + "\n")
    file.close()


# Sorts the list, if reverse is true then sorts in reverse order.
def quick_sort(lst, reverse: bool = False):
    quick_sort_range(lst, 0, len(lst) - 1)
    if reverse:
        lst.reverse()


# Recursive quick sort method.
def quick_sort_range(lst, left: int, right: int):
    if left >= right:
        return
    i = left
    j = right
    mid = lst[left]
    while i <= j:
        while lst[i] < mid:
            i += 1
        while lst[j] > mid:
            j -= 1
        if i <= j:
            (lst[i], lst[j]) = (lst[j], lst[i])
            i += 1
            j -= 1
    if left < j:
        quick_sort_range(lst, left, j)
    if i < right:
        quick_sort_range(lst, i, right)


# Method for testing the execution time of quick sort.
def quick_sort_test(n: int, mn: int, mx: int, increment: int, n_repeat: int):
    for i in range(0, n_repeat):
        lst = generate_list(n, mn, mx)
        start_time = time.time()
        quick_sort(lst)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(n, elapsed_time)
        n += increment
