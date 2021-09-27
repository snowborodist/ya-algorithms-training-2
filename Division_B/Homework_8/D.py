file = open('input_d_10.txt')
lines = file.readlines()
file.close()

n = int(lines[0])
rel_map = {}
nodes_set = set()

for i in range(1, n):
    parent, child = map(int, lines[i].split())

    nodes_set.add(parent)
    nodes_set.add(child)

    if parent not in rel_map:
        rel_map[parent] = [child]
    else:
        rel_map[parent].append(child)

    if child not in rel_map:
        rel_map[child] = [parent]
    else:
        rel_map[child].append(parent)

# print(rel_map)


def find_max_route(start_node, relations):

    depth = 0
    v_nodes = set()
    v_nodes.add(start_node)
    nodes_to_process_next = relations[start_node]

    while nodes_to_process_next:
        np_nodes = []
        for p_node in nodes_to_process_next:
            if p_node not in v_nodes:
                v_nodes.add(p_node)
                np_nodes.extend(relations[p_node])
        nodes_to_process_next = np_nodes
        depth += 1

    return depth


distances = []
for node in nodes_set:
    distances.append(find_max_route(node, rel_map))
print(max(distances))
