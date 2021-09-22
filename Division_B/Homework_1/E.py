import math

d = int(input())
x, y = map(int, input().split())


def solution():
    # проверка на попадание в квадрат:
    if 0 <= x <= d and 0 <= y <= d:
        # в квардате, теперь проверяем на вхождение в треугольник
        if (d - x - y) >= 0:
            return 0

    # если вне треугольника:
    # расстояние между точками:
    point = (x, y)
    distances = [
        math.dist(point, (0, 0)),
        math.dist(point, (d, 0)),
        math.dist(point, (0, d))
    ]
    min_dist = min(distances)

    if min_dist == distances[0]:
        return 1
    elif min_dist == distances[1]:
        return 2
    else:
        return 3


print(solution())
