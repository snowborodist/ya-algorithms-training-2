# TODO: Можно ускорить решение, поменяв ввод на считывание из файла.
import math

n = int(input())

# События, связанные с высотами "прямоугольников"
h_events = [(0.0, 0, 0)] * (n * 2)

# События, связанные с угловой шириной "прямоугольников"
w_events = [(0.0, 0, 0)] * (n * 2)

j = 0

# Коды событий:
# -1: начало отрезка,
#  1: конец отрезка. Такой приоритет, потому что по условию отрезок включает в себя оба конца.

for i in range(n):
    r1, r2, f1, f2 = map(float, input().split())
    f1 = f1 % (math.pi * 2)
    f2 = f2 % (math.pi * 2)
    h_events[j] = (r1, -1, i)
    h_events[j + 1] = (r2, 1, i)
    w_events[j] = (f1, -1, i)
    w_events[j + 1] = (f2, 1, i)
    j += 2

h_events.sort()
w_events.sort()

# 1. Сначала найдем пересечение высот. Тут у нас просто события на прямой.
intersection_count = 0
res_h1 = 0
res_h2 = 0

for h_event in h_events:
    if h_event[1] == -1:
        intersection_count += 1
        if intersection_count == n:
            res_h1 = h_event[0]
    elif h_event[1] == 1:
        if intersection_count == n:
            res_h2 = h_event[0]
        intersection_count -= 1


# 2. Теперь найдем пересечение углов. Тут круговые координаты, так что идем в 2 прохода.

# Тут будем хранить те ширины, для которых мы обработали начало отрезка
started_widths = set()

f_intersections = []
last_max_f1 = 0

for w_event in w_events:
    if w_event[1] == -1:
        started_widths.add(w_event[2])
    elif w_event[1] == 1:
        if w_event[2] in started_widths:
            started_widths.remove(w_event[2])


for w_event in w_events:
    if w_event[1] == -1:
        started_widths.add(w_event[2])
        if len(started_widths) == n:
            last_max_f1 = w_event[0]
    elif w_event[1] == 1:
        if len(started_widths) == n:
            f_intersections.append((last_max_f1, w_event[0]))
        started_widths.remove(w_event[2])

if len(started_widths) == n:
    f_intersections.append((last_max_f1, 2 * math.pi))

# 3. Наконец, вычисляем площадь полярного прямоугольника (он же сектор кольца окружности) по известной формуле.

s = 0
for f_inter in f_intersections:
    div = (f_inter[1] - f_inter[0]) % (2 * math.pi)
    s += (div / 2) * (res_h2 ** 2 - res_h1 ** 2)
print(s)
