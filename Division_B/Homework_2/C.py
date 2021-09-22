import math

input_str = input()


def solution():
    input_str_len = len(input_str)
    if input_str_len == 1:
        return 0
    changes_count = 0
    for i in range(math.floor(input_str_len / 2)):
        if input_str[i] != input_str[input_str_len - i - 1]:
            changes_count += 1
    return changes_count


print(solution())
