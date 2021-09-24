# TODO: Для улучшения производительности можно заменить ввод на чтение из файла.

n, m = map(int, input().split())
kittens = [int(num) for num in input().split()]

# (coord, type, line_index)
events = [(0, 0, 0)] * (2 * m + n)

# (l, r, kitty_count)
lines = [[0, 0, 0]] * m

i = 0

# -1: начало отрезка,
#  1: конец отрезка. Такой приоритет, потому что опо условию отрезок включает в себя оба конца.
#  0: котенок.

for kitty in kittens:
    events[i] = (kitty, 0, -1)
    i += 1

for j in range(m):
    l, r = map(int, input().split())
    lines[j] = [l, r, 0]
    events[i] = (l, -1, j)
    events[i + 1] = (r, 1, j)
    i += 2

events.sort()
kittens_count = 0

for event in events:
    if event[1] == -1:
        lines[event[2]][2] = kittens_count
    elif event[1] == 1:
        lines[event[2]][2] = kittens_count - lines[event[2]][2]
    else:
        kittens_count += 1

print(' '.join([str(elem[2]) for elem in lines]))
