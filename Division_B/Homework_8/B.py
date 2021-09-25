# TODO: Не забудь поменять имя файла на 'input.txt' перед отправкой в контест
file = open('input_b.txt')
lines = file.readlines()
file.close()

n = int(lines[0])

# 1. Заполняем словарь родственников
rel_map = {}
for line in lines[1: n]:
    anc, pre = line.split()
    if pre not in rel_map:
        rel_map[pre] = [anc]
    else:
        rel_map[pre].append(anc)


# 2. Определяем функцию поиска потомка
def rel_exists(predecessor, ancestor):
    re_flag = []

    def rel_exists_recur(p, a, flag: []):
        if p not in rel_map:
            return

        anc_list = rel_map[p]
        if a in anc_list:
            flag.append(True)
            return

        for aa in anc_list:
            if not flag:
                rel_exists_recur(aa, a, flag)

    rel_exists_recur(predecessor, ancestor, re_flag)
    return bool(re_flag)


# 3. Обрабатываем запросы
request_results = []

for request in lines[n:]:
    first, second = request.split()
    if rel_exists(first, second):
        request_results.append('1')
    elif rel_exists(second, first):
        request_results.append('2')
    else:
        request_results.append('0')

# 4. Выводим результаты
print(' '.join(request_results))
