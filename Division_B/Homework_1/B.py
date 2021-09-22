import math

n, i, j = map(int, input().split())


def solution():
    delta = abs(j - i)
    if delta == 1:
        return 0
    if delta <= math.floor(n / 2):
        return delta - 1
    return n - delta - 1


def solution2():
    delta = abs(j - i)
    if delta <= math.floor(n / 2):
        return delta - 1
    return n - delta - 1


print(solution2())
