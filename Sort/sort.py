import random


def generate_list(n: int, mn: int, mx: int):
    """
    Generates a list.
    :param n: number of elements
    :param mn: minimum item value
    :param mx: maximum item value
    :return: list of n elements with integers in the range [mn, mx]
    """
    lst = []
    for i in range(0, n):
        lst.append(random.randint(mn, mx))
    return lst


def write_list_to_file(lst: list, file_name: str):
    """
    Writes the list to a file.
    :param lst: list to write
    :param file_name: name of the file
    :return: None
    """
    file = open(file_name, "w")
    for item in lst:
        file.write(str(item) + "\n")
    file.close()


def get_list_from_file(file_name: str):
    """
    Reads a list from a file.
    :param file_name: name of the file
    :return: list from a file
    """
    file = open(file_name, "r")
    lst = []
    for line in file:
        lst.append(int(line))
    return lst


def quick_sort(lst: list, reverse: bool = False):
    """
    Sorts the list.
    :param lst: list to sort
    :param reverse: if true then sorts in reverse order
    :return: sorted list
    """
    lst_copy = lst.copy()
    quick_sort_range(lst_copy, 0, len(lst_copy) - 1)
    if reverse:
        lst_copy.reverse()
    return lst_copy


def quick_sort_range(lst: list, left: int, right: int):
    """
    Recursive quick sort method.
    :param lst: list to sort
    :param left: index of the left element of the subarray
    :param right: index of the right element of the subarray
    :return: None
    """
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
