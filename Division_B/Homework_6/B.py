def l_bin_search(left, right, check, check_params):

    while left < right:
        m = (left + right) // 2
        if check(m, check_params):
            right = m
        else:
            left = m + 1
    return left


def r_bin_search(left, right, check, check_params):

    while left < right:
        m = (left + right + 1) // 2
        if check(m, check_params):
            left = m
        else:
            right = m - 1
    return left


n = int(input())
nums = [int(num) for num in input().split()]


def check(m, eq):
    return nums[m] >= eq


def r_check(m, eq):
    return nums[m] <= eq


search_n = int(input())
search_nums = [int(num) for num in input().split()]

for i in range(search_n):
    num_to_search = search_nums[i]
    left_i = l_bin_search(0, n - 1, check, num_to_search)
    right_i = r_bin_search(0, n - 1, r_check, num_to_search)

    if nums[left_i] != num_to_search:
        print("0 0")
    else:
        print(f'{left_i + 1} {right_i + 1}')
