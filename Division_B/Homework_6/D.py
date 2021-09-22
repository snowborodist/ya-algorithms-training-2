def l_bin_search(left, right, check, check_params):

    while left < right:
        m = (left + right) // 2
        if check(m, check_params):
            right = m
        else:
            left = m + 1
    return left


a, k, b, m, x = tuple(map(int, input().split()))


def trees_cut(days):
    return a * (days - days // k) + b * (days - days // m)


def check(days, _):
    return trees_cut(days) >= x


print(l_bin_search(0, x, check, ()))
