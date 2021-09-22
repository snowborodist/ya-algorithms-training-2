def solution():
    cur_max = int(input())
    cur_count = 1
    if cur_max == 0:
        return 0
    should_continue = True
    while should_continue:
        pending_num = int(input())
        if pending_num == 0:
            should_continue = False
        elif pending_num > cur_max:
            cur_max = pending_num
            cur_count = 1
        elif pending_num == cur_max:
            cur_count += 1
    return cur_count


print(solution())
