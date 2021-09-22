pars_str = input()


def solution():
    if not pars_str:
        return 'NO'

    w_sum = 0
    for sym in pars_str:
        if sym == '(':
            w_sum += 1
        else:
            w_sum -= 1
            if w_sum < 0:
                return 'NO'
    if w_sum == 0:
        return 'YES'
    return 'NO'


print(solution())
