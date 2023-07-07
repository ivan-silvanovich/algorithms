def gcd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        i = len(arr) // 2
        return sum(arr[:i]) + sum(arr[i:])


def count(arr):
    if not arr:
        return 0
    else:
        return 1 + count(arr[1:])


def max(arr):
    if len(arr) <= 2:
        return arr[0] if arr[0] > arr[-1] else arr[-1]

    i = len(arr) // 2
    left, right = max(arr[:i]), max(arr[i:])
    return left if left > right else right


if __name__ == '__main__':

    # num1 = 1680
    # num2 = 640
    # print(gcd(num1, num2))

    arr = [1, 2, 3, 4, 5]
    print(sum(arr))
    print(count(arr))
    print(max(arr))
