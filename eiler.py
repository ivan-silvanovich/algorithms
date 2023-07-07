import time, functools, itertools
from mpmath import *

# 1
"""now = time.time()
a = [x for x in range(1, 1000) if not (x % 3) or not (x % 5)]
print(sum(a))
print('time: ', time.time() - now)"""

# 2
"""now = time.time()
a = 1
b = 2
sum = 0
while b <= 4000000:
    if not (b % 2):
        sum += b
    a, b = b, a+b
print(sum)
print('time: ', time.time() - now)"""

# 3
"""def simple_list(arr):
    k = 2
    l = len(arr)
    sq = l ** 0.5
    while k < sq:
        if arr[k]:
            for i in range(k ** 2, l, k):
                arr[i] = 0
        k += 1
    return [x for x in arr if (x)][1:]


def search(arr, num):
    for i in arr:
        if not (num % i):
            return i


now = time.time()
num = 600851475143
simple = [x for x in range(round(num ** 0.5))]
simple = simple_list(simple)
print(search(simple[::-1], num))
print('time: ', time.time() - now)"""

# 4
"""def palindrome():
    arr = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            num = i * j
            if str(num) == str(num)[::-1]:
                arr.append(num)
    return max(arr)


now = time.time()
print(palindrome())
print('time: ', time.time() - now)"""

# 5
"""def numbers(num, n):
    for i in range(n+1, int(n / 2), -1):
        if num % i:
            return False
    return True


now = time.time()
num = 20
while not numbers(num, 20):
    num += 20
print(num)
print('time: ', time.time() - now)"""

# 6
"""now = time.time()
print(sum([i for i in range(1, 101)]) ** 2 - sum([i ** 2 for i in range(1, 101)]))
print('time: ', time.time() - now)"""

# 7
"""def simple_list(arr):
    k = 2
    l = len(arr)
    sq = l ** 0.5
    while k < sq:
        if arr[k]:
            for i in range(k ** 2, l, k):
                arr[i] = 0
        k += 1
    return [x for x in arr if (x)][1:]


print(simple_list([x for x in range(110000)])[10000])"""

# 8
"""def mul(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


su = 0
max = 0
max_arr = []
file = open("input.txt")
num = ""
for i in file.read():
    if i != ' ' and i != '\n':
        num += i
for i in range(len(num) - 12):
    arr = [int(i) for i in num[i:i + 13]]
    su = mul(arr)
    if su > max:
        max = su
print(max)"""

# 9
"""def triplet():
    for a in range(1000):
        for b in range(a, 1000):
            c = (a ** 2 + b ** 2) ** 0.5
            if c <= b:
                continue
            if a + b + c == 1000:
                print(a, b, c)
                return a * b * c


print(triplet())"""

# 10
"""def simple_list(arr):
    k = 2
    l = len(arr)
    sq = l ** 0.5
    while k < sq:
        if arr[k]:
            for i in range(k ** 2, l, k):
                arr[i] = 0
        k += 1
    return [x for x in arr if (x)][1:]


print(sum(simple_list([x for x in range(2000000)])))"""

# 12
"""def simple_list(arr):
    k = 2
    l = len(arr)
    sq = l ** 0.5
    while k < sq:
        if arr[k]:
            for i in range(k ** 2, l, k):
                arr[i] = 0
        k += 1
    return [x for x in arr if (x)][1:]
def q(num, simple):
    qu = 1
    arr = []
    i = 0
    while num > 1:
        if num % simple[i] == 0:
            arr.append(simple[i])
            num /= simple[i]
            i -= 1
        i += 1
    s = set(arr)
    for i in s:
        c = 0
        for j in arr:
            if i == j:
                c += 1
        qu *= (c+1)
    return qu
sum = 1
i = 2
l = simple_list([i1 for i1 in range(0, 1000000)])
while q(sum, l) < 500:
    sum += i
    i += 1
print(sum)"""

# 13
"""file = open("input.txt")
file = file.read().split('\n')
print(str(sum([int(i[:11]) for i in file]))[:10])"""

# 14
"""el = 0
max = 0
for i in range(999999, 0, -1):
    k = i
    len = 0
    while k > 1:
        if k % 2:
            k = k * 3 + 1
        else:
            k /= 2
        len += 1
    if len > max:
        max = len
        el = i
    print(i)
print('el ', el)"""

# 15
"""def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(sum([int(i) for i in str(fact(100))]))"""

# 16
"""
print(sum([int(i) for i in str(2 ** 1000)]))
"""

# 17
"""def number(num):
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    dozens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = [""] + [i + " hundred and " for i in digits[1:]]
    thousands = [""] + [i + " thousand and " for i in digits[1:]]
    num = str(num)
    while len(num) < 4:
        num = '0' + num
    if num[2] == '1':
        return thousands[int(num[0])] + hundreds[int(num[1])] + digits[int(num[-2:])]
    elif num[1:] == '000':
        return thousands[int(num[0])][:-5]
    elif num[2:] == '00':
        return thousands[int(num[0])] + hundreds[int(num[1])][:-5]
    return thousands[int(num[0])] + hundreds[int(num[1])] + dozens[int(num[2])] + ' ' + digits[int(num[3])]
def space_del(s):
    s1 = ""
    for i in s:
        if i == ' ':
            continue
        s1 += i
    return s1
print(sum([len(space_del(number(i))) for i in range(1, 1001)]))"""

# 18
"""maxi = 0
def way(arr, j=0, i=0, sum=0):
    global maxi, ways
    sum += arr[i][j]
    if sum > maxi:
        maxi = sum
    if i + 1 == len(arr):
        return 0
    way(arr, j, i+1, sum)
    way(arr, j+1, i+1, sum)
triangle = [[int(j) for j in i.split(' ') if j] for i in [i for i in open('input.txt').read().split('\n') if i]]
way(triangle)
print(maxi)"""

# 20
"""def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(sum([int(i) for i in str(fact(100))]))"""

# 22
"""def maxi(name1, name2):
    n = ""
    for i in name1: n += str(ord(i))
    print(n, name1)
    name1 = int(n)
    n = ""
    for i in name2: n += str(ord(i))
    name2 = int(n)
    if name1 > name2: return True
    else : return False
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = int(len(arr) / 2)
        less, gather = [], []
        value = arr[mid]
        for i in arr:
            if i == arr[mid]: continue
            elif maxi(arr[mid], i):  less.append(i)
            else:   gather.append(i)
        return quick_sort(less) + [value] + quick_sort(gather)
def name_score(name):
    score = 0
    for i in name:
        score += ord(i) - 64
    return score
file = open("input.txt")
file = eval('[' + file.read() + ']')
now = time.time()
file = quick_sort(file)
print("time: ", time.time() - now)
print(file)
all_score = 0
for i in range(len(file)):
    all_score += name_score(file[i]) * (i + 1)
print(all_score)
print(maxi('ZBBY', 'ABBY'))"""

# 24
"""combinations = list(itertools.permutations('0123456789'))
for i in combinations[999999]: 
    print(i, end='')"""


# 25
"""a, b, sum, count = 1, 2, 0, 3
while len(str(b)) < 1000: a, b = b, a+b; count += 1;
print(b, count, sep='\n')"""

# 26
mp.dps = 128
a = mpf(1)
b = mpf(7)
print(a/b)
