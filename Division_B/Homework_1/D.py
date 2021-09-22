import math

n = int(input())
coords = [int(coord) for coord in input().split()]


def solution():
    if n == 0:
        return 0
    if n == 1:
        return coords[0]

    if n % 2 == 0:
        return coords[int(n / 2 - 1)]
    else:
        return coords[math.ceil(n / 2) - 1]


print(solution())
