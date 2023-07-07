import random, time, collections


'''def Bin(li, x, i=0, j=len(li) - 1):
    m = int((i + j) / 2)
    if i > j:
        return None
    elif list[m] == x:
        return m
    elif x > list[m]:
        i = m + 1
        return Bin(list, x, m+1, j)
    else:
        j = m
        return Bin(list, x, i, m)'''


def countdown(i):
    print(i)
    if i == 0:
        return
    else:
        countdown(i-1)


def trunc(a):
    return int(a) if a - int(a) < 0.5 else int(a) + 1


def binary(list, num):
    count = 1
    mid = round((len(list) - 1) / 2)
    q = mid
    while q > 0:
        q = round(q / 2)
        print(q, mid)
        value = list[mid]
        if value > num:
            mid -= q
        elif value < num:
            mid += q
        if value == num:
            print(q, mid)
            return (mid, count)
        count += 1
    return None


def BinSearch(li, x):
    counter = 1
    i = 0
    j = len(li) - 1
    while i <= j:
        m = int((i + j)/2)
        print(m, counter)
        if x == li[m]:
            return (m, counter)
        elif x > li[m]:
            i = m + 1
        else:
            j = m
        counter += 1
    return None


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = int(len(arr) / 2)
        value = []
        less = []
        gather = []
        for i in arr:
            if i == arr[mid]:   value.append(i)
            elif i < arr[mid]:  less.append(i)
            else:   gather.append(i)
        # value = [i for i in arr if i == arr[mid]]
        # less = [i for i in arr if i < arr[mid]]
        # gather = [i for i in arr if i > arr[mid]]
        return quick_sort(less) + value + quick_sort(gather)


def simple_sort(arr):
    for i in range(len(arr)):
        value = min(arr[i:])
        arr[arr[i:].index(value) + i] = arr[i]
        arr[i] = value


"""a = [i for i in range(8)]
print(a)
print(BinSearch(a, 7))
countdown(10)
b = [random.randint(0, 10000000) for i in range(10000000)]
now = time.time()
print(b)
c = quick_sort(b)
print('time: ', time.time() - now)
now = time.time()
b.sort()
print('time: ', time.time() - now)
print(b == c)"""


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)
