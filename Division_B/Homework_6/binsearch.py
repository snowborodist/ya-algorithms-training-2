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


def f_bin_search(left, right, eps, check, params):
    while left + eps < right:
        m = (left + right) / 2
        if check(m, eps, params):
            right = m
        else:
            left = m
    return left
