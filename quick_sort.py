import random
import time

from selection_sort import is_smaller


def quick_sort(arr, reverse=False):
    if len(arr) < 2:
        return arr

    base_el = arr.pop(len(arr) // 2)
    # base_el = arr[len(arr) // 2]
    left, right = [], []
    for el in arr:
        if is_smaller(el, base_el, reverse=reverse):
            left.append(el)
        else:
            right.append(el)

    return quick_sort(left, reverse) + [base_el] + quick_sort(right, reverse)


if __name__ == '__main__':

    random.seed(1)

    a = 0
    b = 1000000
    # numbers = [i for i in range(a, b + 1)]
    numbers = [random.randint(a, b) for i in range(b)]
    # print(numbers)

    start = time.time()
    numbers = quick_sort(numbers, reverse=True)
    print(time.time() - start)
    # print(numbers)
