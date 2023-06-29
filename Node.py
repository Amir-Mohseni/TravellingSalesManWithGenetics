class Node:
    def __init__(self, index, name):
        self.name = name
        self.index = index
        self.edges = []

    def add_edge(self, e):
        self.edges.append(e)

    def print_node(self):
        print("Node name:", self.name, "&", "Node index:", self.index + 1, sep=' ')
        print("Edge List:")
        for edge in self.edges:
            edge.print_edge()
