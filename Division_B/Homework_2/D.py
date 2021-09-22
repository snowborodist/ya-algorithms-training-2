import math

l, k = map(int, input().split())
legs = [int(leg) for leg in input().split()]


def solution():
    if k == 1:
        return legs[0]

    len_is_odd = l % 2 != 0
    mid_of_bench = math.floor(l / 2)
    last_leg_index = 0

    for i in range(k):
        if legs[i] < mid_of_bench:
            last_leg_index = i
        elif legs[i] == mid_of_bench:
            if len_is_odd:
                return legs[i]
            else:
                return f"{legs[last_leg_index]} {legs[i]}"
        else:
            return f"{legs[last_leg_index]} {legs[i]}"


print(solution())
