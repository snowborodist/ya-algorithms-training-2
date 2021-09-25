# TODO: Не забудь поменять имя файла на 'input.txt' перед отправкой в контест
file = open('input_c.txt')
lines = file.readlines()
file.close()

n = int(lines[0])

# 1. Заполняем словарь родственников и попутно определяем корень дерева
#    (у корня дерева нет родителя, соответственно его не будет в списке всех
#    встреченных во время заполнения словаря детей).

rel_map = {}
anc_set = set()
root = None

for line in lines[1: n]:
    anc, pre = line.split()
    anc_set.add(anc)

    if pre not in anc_set:
        root = pre
    if pre not in rel_map:
        rel_map[pre] = [anc]
    else:
        rel_map[pre].append(anc)


# 2. Далее необходимо построить дерево для работы алгоритма LCA
#    Для этого определим рекурсивную функцию прохода по словарю родственников:

def fill_tree(tree_list, root_key, relations_map, predecessor=None, depth=0):
    # Формат узла:
    # [Ключ, [Список_Потомков], Предок, Глубина_узла]

    node = [root_key, [], predecessor, depth]
    tree_list.append(node)

    if root_key not in relations_map:
        return

    for rel in relations_map[root_key]:
        fill_tree(node[1], rel, relations_map, node, depth + 1)


# 3. Строим дерево:
tree = []
fill_tree(tree, root, rel_map)

# from pprint import pprint
# pprint(tree)

# 4. Определяем функцию LCA (Lowest Common Ancestor, Наименьший Общий Предок)


# TODO: Написать функцию LCA
def lca(person_a, person_b) -> str:
    pass


# 5. Обрабатываем запросы и выводим результаты

for request in lines[n:]:
    first_person, second_person = request.split()
    print(lca(first_person, second_person))
