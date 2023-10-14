from sort import *


def check_sorting():
    input_lst = generate_list(10, -100, 100)
    generate_file(input_lst, "input.txt")
    lst = get_list_from_file("input.txt")
    print("Input: ", lst)
    sorted_list = quick_sort(lst)
    write_list_to_file(sorted_list, "output.txt")
    print("Output: ", sorted_list)


def check_time():
    quick_sort_test(100000, -1000000000, 1000000000, 100000, 10000)


if __name__ == '__main__':
    check_sorting()
    # check_time()
