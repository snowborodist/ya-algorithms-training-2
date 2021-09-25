def add(root, key):
    if not root:
        root.extend([key, None, None])
        print("DONE")
        return

    root_key = root[0]
    if key == root_key:
        print("ALREADY")
        return
    elif key < root_key:
        left_anc = root[1]
        if not left_anc:
            root[1] = [key, None, None]
            print("DONE")
        else:
            add(root[1], key)
    elif key > root_key:
        right_anc = root[2]
        if not right_anc:
            root[2] = [key, None, None]
            print("DONE")
        else:
            add(root[2], key)


def search(root, key):
    if not root:
        print("NO")
        return

    root_key = root[0]
    if key == root_key:
        print("YES")
        return
    elif key < root_key:
        left_anc = root[1]
        if not left_anc:
            print("NO")
        else:
            search(left_anc, key)
    elif key > root_key:
        right_anc = root[2]
        if not right_anc:
            print("NO")
        else:
            search(root[2], key)


def walk(root, depth=0):
    if not root:
        return

    if root[1]:
        walk(root[1], depth + 1)
    print(f"{''.join('.' * depth)}{root[0]}")
    if root[2]:
        walk(root[2], depth + 1)


file = open('input_a_3.txt')
commands = file.readlines()
file.close()

tree = []

for command in commands:
    command_parts = command.split()

    if command_parts[0] == 'ADD':
        add(tree, int(command_parts[1]))
    elif command_parts[0] == 'SEARCH':
        search(tree, int(command_parts[1]))
    elif command_parts[0] == 'PRINTTREE':
        walk(tree)
