def l_bin_search(left, right, check, check_params):
    while left < right:
        m = (left + right) // 2
        if check(m, check_params):
            right = m
        else:
            left = m + 1
    return left


file = open("input.txt")
n, k = map(int, file.readline().split())
nums = sorted([int(num) for num in file.readline().split()])
file.close()

min_num = nums[0] - 1
nums = [num - min_num for num in nums]


def check(l_num, _):
    count = 1
    cur_start = nums[0]
    for num in nums:
        if (num - cur_start) > l_num:
            cur_start = num
            count += 1
            if count > k:
                return False
    return count <= k


print(l_bin_search(0, nums[-1], check, ()))
