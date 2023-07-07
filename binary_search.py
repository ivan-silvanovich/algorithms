import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'time: {time.time() - start}')
        return result
    return wrapper


@benchmark
def binary_search(arr, obj) -> tuple:
    """
    Function gets two elements:

        binary_search(arr, obj)

        arr: an iterable object containing sorted elements
        obj: the element which the function is looking for

    Function returns a tuple containing two elements:

        (steps, index)

        steps: an amount of search operations to reach the element
        index: the index of the found element or None in the case of absence
    """

    begin, end = -1, len(arr)
    steps = 0

    while True:
        steps += 1

        mid = (begin + end) // 2
        if end - begin == 1:
            return steps - 1, None
        elif arr[mid] > obj:
            end = mid
        elif arr[mid] < obj:
            begin = mid
        else:
            return steps, mid


@benchmark
def binary_search2(list, item):
    low, high = 0, len(list) - 1
    steps = 0

    while low <= high:
        steps += 1

        mid = (low + high) // 2
        if list[mid] == item:
            return steps, mid
        if list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return steps, None


def binary_search3(arr, obj, const=0, steps=0):
    if len(arr) == 1:
        return steps, const if arr[0] == obj else None

    mid = len(arr) // 2
    if arr[mid] == obj:
        return steps, mid + const
    elif arr[mid] > obj:
        return binary_search3(arr[:mid], obj, const=const, steps=steps + 1)
    else:
        return binary_search3(arr[mid + 1:], obj, const=const + mid + 1, steps=steps + 1)


if __name__ == '__main__':

    function = binary_search3

    a = 0
    b = 8
    numbers = [i for i in range(a + 1, b + 1)]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # number = int(input('Enter a number: '))
    # result = function(numbers, number)
    # print(result)
    #
    # number = input('Enter a char: ')
    # result = function(letters, number)
    # print(result)
    #
    #
    for num in range(a + 1, b + 1):
        print(function(numbers, num))
    #
    # print('start')
    # start = time.time()
    # print(function(numbers, 1))
    # print(f'time: {time.time() - start}')
    #
    # for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #     steps, index = function(letters, ch)
    #
    #     if ch in letters:
    #         answer = letters.index(ch)
    #     else:
    #         answer = None
    #
    #     print((steps, index), 'OK' if index == answer else 'FAIL')
