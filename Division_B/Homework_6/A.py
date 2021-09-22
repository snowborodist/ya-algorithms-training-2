# TODO: Можно решить с двумя левыми поисками, один больше-вавно, и другой строго больше

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
nums = sorted([int(num) for num in input().split()])


def check(m, eq):
    return nums[m] >= eq


def r_check(m, eq):
    return nums[m] <= eq


check_n = int(input())
ans = ['0'] * check_n

for i in range(check_n):
    l, r = map(int, input().split())
    left_i = l_bin_search(0, n - 1, check, l)
    right_i = r_bin_search(0, n - 1, r_check, r)
    count = right_i - left_i + 1
    if (left_i == right_i == 0 and nums[0] > r) or (left_i == right_i == (n - 1) and nums[n-1] < l):
        ans[i] = '0'
    else:
        ans[i] = str(count)

print(' '.join(ans))
