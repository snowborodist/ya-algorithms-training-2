def f_bin_search(left, right, eps, check, params):
    while left + eps < right:
        m = (left + right) / 2
        if check(m, eps, params):
            right = m
        else:
            left = m
    return left


def eq(x, params):
    a, b, c, d = params
    return a * x**3 + b * x**2 + c * x + d


def check_pos(x, eps, params):
    return eq(x, params) > 0


def check_neg(x, eps, params):
    return eq(x, params) < 0


parameters = tuple(map(int, input().split()))
epsilon = 0.0000001

if parameters[0] > 0:
    print(f_bin_search(-1000000, 1000000, epsilon, check_pos, parameters))
else:
    print(f_bin_search(-1000000, 1000000, epsilon, check_neg, parameters))
