import sys
sys.setrecursionlimit(1200)

# TODO: Не забудь поменять имя файла на 'input.txt' перед отправкой в контест
file = open('input_c_12.txt')
lines = file.readlines()
file.close()

n = int(lines[0])

# 1. Заполняем словарь родственников и попутно определяем корень дерева
#    (у корня дерева нет родителя, соответственно его не будет в списке всех
#     встреченных во время заполнения словаря детей).

rel_tree_index = {}
rel_map = {}
anc_set = set()
all_set = set()

for line in lines[1: n]:
    anc, pre = line.split()
    anc_set.add(anc)
    all_set.add(anc)
    all_set.add(pre)

    if pre not in rel_map:
        rel_map[pre] = [anc]
    else:
        rel_map[pre].append(anc)

root = list(all_set.difference(anc_set))[0]

# 2. Далее необходимо построить дерево для работы алгоритма LCA
#    Для этого определим рекурсивную функцию прохода по словарю родственников:


# TODO: Тут можно добавить проверку, что в дереве нет циклических зависимостей
def fill_tree(tree_list, root_key, relations_map, predecessor=None, depth=0):
    global rel_tree_index
    # Формат узла:
    # [Ключ, [Список_Потомков], Предок, Глубина_узла]
    node = [root_key, [], predecessor, depth]
    tree_list.append(node)

    # Здесь заполняем индекс для быстрого поиска узлов дерева по ключу:
    rel_tree_index[root_key] = node

    if root_key not in relations_map:
        return

    for rel in relations_map[root_key]:
        fill_tree(node[1], rel, relations_map, node, depth + 1)


# 3. Строим дерево:
tree = []
fill_tree(tree, root, rel_map)
tree = tree[0]

# Можно визуализировать результат:
# from pprint import pprint
# pprint(tree, indent=4)

# 4. Определяем функции search и LCA (Lowest Common Ancestor, Наименьший Общий Предок)


# Тут используем ранее построенный индекс для быстрого поиска:
def search(key_to_find):
    if key_to_find not in rel_tree_index:
        return None
    return rel_tree_index[key_to_find]


def lca(person_a, person_b) -> str:
    # Ищем узлы в дереве по ключу.
    node_a = search(person_a)
    node_b = search(person_b)

    # Если один из узлов = корень дерева, то он является
    # наименьшим общим предком для самого себя и другого узла.
    if node_a[3] == 0:
        return node_a[0]
    if node_b[3] == 0:
        return node_b[0]

    # Иначе выбираем узел с большей глубиной
    # и поднимаемся из него до глубины второго узла.
    depth_div = node_a[3] - node_b[3]
    if depth_div > 0:
        for i in range(depth_div):
            node_a = node_a[2]
    elif depth_div < 0:
        for i in range(-depth_div):
            node_b = node_b[2]

    # Теперь синхронно поднимаемся из узлов в родителей, пока не совпадут их ключи
    # (это будет признаком того, что обе переменные указывают на один и тот же узел,
    #  который в следствие этого и является наименьшим общим предком).
    while node_a[0] != node_b[0]:
        node_a = node_a[2]
        node_b = node_b[2]

    return node_a[0]


# 5. Обрабатываем запросы и выводим результаты:
for request in lines[n:]:
    first_person, second_person = request.split()
    print(lca(first_person, second_person))
