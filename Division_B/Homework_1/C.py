x, y, _ = map(int, input().split())


def solution():
    if x <= 12 and y <= 12:
        if x != y:
            return 0
    return 1


print(solution())
