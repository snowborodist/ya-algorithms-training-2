addr_book = [int(addr) for addr in input().split()]


def solution():
    shop_ids = []
    house_ids = []
    for i in range(len(addr_book)):
        if addr_book[i] == 2:
            shop_ids.append(i)
        elif addr_book[i] == 1:
            house_ids.append(i)
    min_max_dist = 0
    for house_id in house_ids:
        min_dist = abs(house_id - shop_ids[0])
        for shop_id in shop_ids:
            cur_dist = abs(house_id - shop_id)
            if cur_dist < min_dist:
                min_dist = cur_dist
        if min_dist > min_max_dist:
            min_max_dist = min_dist
    return min_max_dist


print(solution())
