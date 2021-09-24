# TODO: Решение не проходит по TL, валится на тесте 35, если запускать на 'Python 3.9.1',
#       но отлично отрабатывает на 'Python 3.7 (PyPy 7.3.3)' с огромным запасом по времени:
#
#       Логи тестов:
#       35	ok	3.329s / 29.60Mb	                - Python 3.7 (PyPy 7.3.3)
#       35	time-limit-exceeded	15.021s / 5.87Mb	- Python 3.9.1
#

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
