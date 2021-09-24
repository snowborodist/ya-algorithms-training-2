m = int(input())

events = []

# -1 - событие начала отрезка,
#  1 - событие конца отрезка.
#  0 - событие в точках 0 и m, в которых мы смотрим, какие отрезки покрывают эти точки
LINE_START = -1
LINE_END = 1
BREAKPOINT = 0

# приоритет выбрал исходя из того, что отрезок включает в себя обе границы ([l, r] в условии задачи).
# у события проверки приоритет 0 выбран по той же причине, что и приоритеты событий конца и начала отрезков.

# TODO: Для повышения производительности можно зачитать все из файла.
#  В таком случае можно также заранее аллоцировать память для списка событий.

should_continue = True
lines = []
i = 0

while should_continue:
    ll, rr = map(int, input().split())
    if ll == rr == 0:
        should_continue = False
    else:
        events.append((ll, LINE_START, i))
        events.append((rr, LINE_END, i))
        lines.append((ll, rr))
        i += 1

events.append((0, BREAKPOINT, -1))
events.append((m, BREAKPOINT, -1))
events.sort()

# Логика алгоритма:
# 1. Начинаем стандартным образом перебирать события, пока не доходим до особого события в точке начала отрезка [0,m]
# 2. В точке 0 (при наступлении события BREAKPOINT) смотрим в список текущих пересекающих эту точку отрезков
#    и выбираем из них тот, у которого наибольшее значение правой границы. Добавляем этот отрезок в итоговый список,
#    и ставим следующую контрольную точку в значение его правой границы.
# 3. Доходим до следующей контрольной точки (она проверяется в событии LINE_END),
#    снова смотрим в список текущих событий и выбираем то, у которого наибольшее значение правой границы.
#    Снова добавляем этот отрезок к итогам и обновляем контрольную точку.
# 4. Повторяем процесс до дех пор, пока новая контрольная точка не станет больше или равна m.
# 5. Если в любой из контрольных точек окажется, что список текущих событий пуст,
#    это будет означать, что решения нет.
# 6. Если мы добрались до события BREAKPOINT в точке m, то решения нет (иначе сработало бы условие из п. 4).

current_lines = set()
selected_lines = set()
next_coord = 0


def add_appropriate():
    global next_coord, selected_lines

    if not current_lines:
        selected_lines = set()
        return False

    sorted_current = sorted(current_lines, key=lambda x: x[1], reverse=True)
    appropriate_one = sorted_current[0]
    selected_lines.add(appropriate_one)
    next_coord = appropriate_one[1]

    if next_coord >= m:
        return False

    return True


for event in events:
    coord, event_type, line_index = event
    line = lines[line_index]

    if event_type == LINE_START:
        current_lines.add(line)

    elif event_type == LINE_END:
        if line in current_lines:
            current_lines.remove(line)
        if coord == next_coord:
            if not add_appropriate():
                break

    else:
        if coord == 0:
            if not add_appropriate():
                break
        else:
            if not current_lines:
                selected_lines = set()
            break

if not selected_lines:
    print("No solution")
else:
    print(len(selected_lines))
    print('\n'.join([f"{ll} {rr}" for ll, rr in sorted(list(selected_lines))]))
