n = int(input())

events = [(0, 0)] * (2 * n)
j = 0

# Тут все стандартно, для понимания достаточно посмотреть шестую лекцию.

# -1 - событие начала окрашенного участка
#  1 - событие конца окрашенного участка

for i in range(n):
    l, r = map(int, input().split())
    events[j] = (l, -1)
    events[j + 1] = (r, 1)
    j += 2

events.sort()

layers_count = 0
painted_len = 0

for i in range(2 * n):
    if layers_count > 0:
        painted_len += events[i][0] - events[i - 1][0]
    if events[i][1] == -1:
        layers_count += 1
    else:
        layers_count -= 1

print(painted_len)
