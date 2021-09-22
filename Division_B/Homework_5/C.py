n, m = map(int, input().split())

groups = sorted([(int(group) + 1, index) for index, group in enumerate(input().split())], reverse=True)
rooms = sorted([(int(room), index) for index, room in enumerate(input().split())], reverse=True)

cur_group = 0
cur_room = 0
schedule = ['0'] * n
distributed = 0

while cur_group < n:  # or (cur_room < m)
    if groups[cur_group][0] <= rooms[cur_room][0]:
        schedule[groups[cur_group][1]] = str(rooms[cur_room][1] + 1)
        cur_group += 1
        cur_room += 1
    else:
        cur_group += 1

print(cur_room)
print(' '.join(schedule))
