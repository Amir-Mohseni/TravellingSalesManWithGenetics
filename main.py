from Node import Node
from Edge import Edge


def get_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()

        n, m = map(int, lines[0].split())
        nodes = []

        for i in range(n):
            name = str(lines[i + 1])
            node = Node(i, name)
            nodes.append(node)

        for i in range(m):
            line = lines[i + n + 1].split()
            v = nodes[int(line[0]) - 1]
            u = nodes[int(line[1]) - 1]
            w = int(line[2])
            edge_1 = Edge(i * 2, v, u, w)
            edge_2 = Edge(i * 2 + 1, u, v, w)
            v.add_edge(edge_2)
            u.add_edge(edge_1)
        return n, m, nodes

def fitness(n, m, nodes, adj_list, path):
    seen = [False] * n
    path_weight = 0
    for i in range(n - 1):
        cur_node = path[i]
        next_node = path[i + 1]
        for edge in cur_node.edges:
            if edge.end_point == next_node:
                path_weight += edge.weight
                seen[edge.end_point] = True
                break

def naive_solution(n, m, nodes):
    permutation = []
    for i in range(n):
        permutation.append(i)
    


path = 'input.txt'
n, m, nodes = get_input(path)
INF = int(1e9)
adj_list = [[]] * n
for i in range(n):
    adj_list[i] = [INF] * n
    node = nodes[i]
    for edge in node.edges:
        adj_list[i][edge.end_point.index] = edge.weight
    print(adj_list[i])

