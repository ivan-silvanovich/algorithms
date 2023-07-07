import random
import time


def is_smaller(a, b, reverse: bool = False) -> bool:
    """
    Bool function to figure out which element is greater

    :param a: the first element for comparison
    :param b: the second element for comparison
    :param reverse: bool parameter, when True, the function finds bigger element, default - False
    :return:
    """

    return a > b if reverse else a < b


def get_min_max_element(arr, start: int = 0, end: int = None, max: bool = False) -> tuple:
    """
    A function that returns max or min element of sequence, depending on the arguments

    :param arr: iterable object
    :param start: integer param defines the first index to iterate, default - 0
    :param end: integer param defines the last index to iterate, default - None
    :param max: bool param, inverts instructions to find max element instead of min, default - False
    :return: tuple, contains min(max) element and its index
    """

    end = len(arr) if not end else end
    element, index = arr[start], start

    for i in range(start + 1, end):
        if is_smaller(arr[i], element, reverse=max):
            element = arr[i]
            index = i

    return element, index


def selection_sort(arr: list, reverse: bool = False) -> None:
    """
    The function implements selection sorting algorithm

    :param arr: iterable mutable object
    :param reverse: bool param to invert sorted sequence, default value - False
    :return: None
    """

    for i in range(len(arr)):
        element, index = get_min_max_element(arr, start=i, max=reverse)
        arr[i], arr[index] = arr[index], arr[i]
        # arr.insert(i, arr.pop(index))


if __name__ == '__main__':

    amount = 10000
    a = 0
    b = 10000

    numbers = [random.randint(a, b) for i in range(amount)]
    # numbers = [i for i in range(amount)]
    # print(numbers)

    start = time.time()
    selection_sort(numbers, reverse=False)
    print(time.time() - start)
    print(numbers)
