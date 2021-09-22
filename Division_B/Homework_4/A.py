box_count = int(input())
col_cnt = {}

for _ in range(box_count):
    color, value = map(int, input().split())
    if color in col_cnt:
        col_cnt[color] += value
    else:
        col_cnt[color] = value

for key, value in sorted(col_cnt.items()):
    print(f"{key} {value}")
