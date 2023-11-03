import sys
import time
from sort import *
import matplotlib.pyplot as plt


def check_sorting(n: int, mn: int, mx: int):
    """
    Method for testing quick sort.
    :param n: number of elements
    :param mn: minimum item value
    :param mx: maximum item value
    :return: None
    """
    try:
        input_lst = generate_list(n, mn, mx)
        write_list_to_file(input_lst, "input.txt")
        lst = get_list_from_file("input.txt")
        print("Input: ", lst)
        sorted_list = quick_sort(lst)
        write_list_to_file(sorted_list, "output.txt")
        print("Output: ", sorted_list)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    except OSError:
        print("OS error occurred trying to open file.")
        sys.exit(1)
    except ValueError:
        print("The input file has an incorrect format.")
        sys.exit(1)
    except Exception as err:
        print("Unexpected error opening file is", repr(err))
        sys.exit(1)


def measure_time(n: int, mn: int, mx: int, increment: int, n_repeat: int):
    """
    Method for measuring the execution time of quick sort.
    :param n: number of elements
    :param mn: minimum item value
    :param mx: maximum item value
    :param increment: number by which the amount of items in the list increases with each step
    :param n_repeat: number of steps
    :return: None
    """
    x = []
    y = []
    for i in range(0, n_repeat):
        lst = generate_list(n, mn, mx)
        start_time = time.time()
        quick_sort(lst)
        end_time = time.time()
        elapsed_time = end_time - start_time
        x.append(n)
        y.append(elapsed_time)
        n += increment
    plt.plot(x, y)
    plt.title("Quick sort")
    plt.xlabel("N")
    plt.ylabel("Time, s")
    plt.show()


if __name__ == '__main__':
    print("1. Check sorting")
    print("2. Measure time")
    inp = input("Select an option: ")
    if inp == "1":
        check_sorting(10, -100, 100)
    elif inp == "2":
        measure_time(50000, -1000000000, 1000000000, 50000, 10)
    else:
        print("Unknown option")
