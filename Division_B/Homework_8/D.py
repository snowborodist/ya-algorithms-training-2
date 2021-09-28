# TODO: Не забудь поменять ввод на 'input.txt'
file = open('input_d_12.txt')
lines = file.readlines()
file.close()

n = int(lines[0])
rel_map = {}

# 1. Заполняем map со связями между узлами:
for i in range(1, n):
    parent, child = map(int, lines[i].split())

    if parent not in rel_map:
        rel_map[parent] = [child]
    else:
        rel_map[parent].append(child)

    # Заполняем связи в обратную сторону,
    # так как по условию у нас неориентированный граф:
    if child not in rel_map:
        rel_map[child] = [parent]
    else:
        rel_map[child].append(parent)


# 2. Определяем функцию поиска листов дерева
#    (или по-другому - конечных точек нецикличного неориентированного графа).
#    Признак листа - всего одна связь с другим узлом.
def get_leaves():
    leaves_list = []
    for node in rel_map:
        if len(rel_map[node]) == 1:
            leaves_list.append(node)
    return leaves_list


# 3. Определяем функцию поиска диаметра дерева (наибольшего пути графа).
#    Идея заключается в том, чтобы каждый раз находить листы дерева,
#    затем удалять их из дерева и добавлять к искомому значению 2,
#    пока в дереве не останется меньше двух элементов.
#    После этого прибавляем еще 1, если остался один (нечетный корневой) элемент, и выводим результат.
#
#    Тут стоит отдельно отметить, что наибольший путь в таком дереве (или ацикличном ненаправленном графе)
#    это всегда путь от одного листа до другого через его корень.
#    Прибавляем 2, а не 1, потому что удаляя листья, мы на каждом этапе
#    сокращаем наш искомый наибольший путь сразу на 2 элемента.

def find_diameter():
    global rel_map
    dist = 0

    while len(rel_map) >= 2:
        leaves = get_leaves()
        for leaf in leaves:
            for leaf_child in rel_map[leaf]:
                rel_map[leaf_child].remove(leaf)
            rel_map.pop(leaf)
        if len(leaves) < 2:
            dist += 1
        else:
            dist += 2

    dist += len(rel_map)

    print(dist)


find_diameter()
