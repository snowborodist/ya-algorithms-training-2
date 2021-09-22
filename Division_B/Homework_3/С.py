sequence = input().split()


def solution():
    all_nums = set()
    not_uniques = set()

    for num in sequence:
        if num not in all_nums:
            all_nums.add(num)
        else:
            not_uniques.add(num)

    uniques = all_nums.difference(not_uniques)
    return [num for num in sequence if num in uniques]


print(' '.join(solution()))
