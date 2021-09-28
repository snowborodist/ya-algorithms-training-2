# TODO: Не забудь поменять ввод на 'input.txt'!
file = open('inputs/input_e.txt')
lines = file.readlines()
file.close()


# 1. Определяем простую рекурсивную функцию обхода дерева в глубину
#    (по дороге строим текущий путь, который добавляем к результатам
#     при достижении листа дерева):
def walk(tree_root, res, path=""):
    if tree_root[0]:
        walk(tree_root[0], res, f"{path}{0}")
    if not tree_root[0] and not tree_root[1]:
        res.append(f"{path}\n")
    if tree_root[1]:
        walk(tree_root[1], res, f"{path}{1}")


# Вывод большой, так что будем записывать его в файл:
outfile = open('output.txt', 'w')

# 2. Далее идем по кодам деревьев и разворачиваем их в сами деревья
#    по правилам, указанным в условии задачи:
for input_line in lines[1:]:
    commands = [char for char in input_line]

    # Формат узла: [left_subtree, right_subtree, parent, child_type]
    # Тип потомка (child_type): -1 для левого, and 1 для правого.
    tree = [[[], [], None, 0]]
    root = tree[0]
    current = root

    for command in commands:
        if command == 'D':
            new_elem = [[], [], current, -1]
            current[0] = new_elem
            current = new_elem
        elif command == 'U':
            while current[3] == 1:
                current = current[2]
            current = current[2]
            new_elem = [[], [], current, 1]
            current[1] = new_elem
            current = new_elem

    tree = tree[0]

    # 3. Для каждого построенного дерева совершаем обход и выводим результаты:
    results = []
    walk(tree, results)
    # print(len(results))
    outfile.write(f"{len(results)}\n")
    # for result in results:
    #     print(result)
    outfile.writelines(results)

outfile.close()
