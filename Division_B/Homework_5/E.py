# TODO: Решение не проходит по TL, валится на тесте 35.

s = int(input())

a_raw = [int(num) for num in input().split()]
a_len = a_raw[0]
a = a_raw[1:]

b_raw = [int(num) for num in input().split()]
b_len = b_raw[0]
b = b_raw[1:]

c_raw = [int(num) for num in input().split()]
c_len = c_raw[0]
c = c_raw[1:]

c_map = {}
for index, elem in enumerate(c_raw[1:]):
    if elem not in c_map:
        c_map[elem] = index


def solution():
    for i in range(len(a)):
        for j in range(len(b)):
            num_to_find = s - a[i] - b[j]
            if num_to_find in c_map:
                return f"{i} {j} {c_map[num_to_find]}"
    return "-1"


print(solution())
