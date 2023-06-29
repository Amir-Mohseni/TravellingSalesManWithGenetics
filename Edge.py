class Edge:
    def __init__(self, index, v, u, w):
        self.index = index
        self.start_point = v
        self.end_point = u
        self.weight = w

    def print_edge(self):
        print("Edge Index:", self.index + 1, "StartPoint:", self.start_point.name, "EndPoint", self.end_point.name, "Weight:", self.weight)

