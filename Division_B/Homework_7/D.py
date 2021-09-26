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

# Идея решения:
# 1. Создаем список отрезков lines со счетчиками количества котят, установленными в 0.
# 2. Также заполняем список событий (events), указывая в них ссылки-ииндексы соответствующих им отрезков из lines.
# 3. Каждый раз при встрече котенка увеличиваем счетчик котят kitten_count.
# 4. При возникновении события начала отрезка устанавливаем счетчик котят соответствующего ему отрезка
#    в текущее значение kitten_count.
# 5. При возникновении события конца отрезка обновляем значение счетчика котят соответствующего ему отрезка:
#    lines[event[2]][2] = kittens_count - lines[event[2]][2] (текущее количество котят - записанное ранее количество)
#    - это значение и будет равно количеству котят на отрезке.


for event in events:
    if event[1] == -1:
        lines[event[2]][2] = kittens_count
    elif event[1] == 1:
        lines[event[2]][2] = kittens_count - lines[event[2]][2]
    else:
        kittens_count += 1

print(' '.join([str(elem[2]) for elem in lines]))
