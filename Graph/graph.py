class Graph:

    def __init__(self, node_count: int, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if not adj_list:  # if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def degree_out(self, u: int) -> int:  # grau de saída
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:  # grau de entrada
        degree = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                degree += 1
        return degree

    def highest_degree_out(self) -> int:  # nó com o maior grau de saída
        max_degree_out = 0
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_out_node_i = self.degree_out(i)
            if max_degree_out < degree_out_node_i:
                max_degree_out = degree_out_node_i
                highest_degree_node = i
        return highest_degree_node

    def highest_degree_in(self) -> int:  # nó com o maior grau de entrada
        max_degree_in = float("inf")
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_in_node_i = self.degree_in(i)
            if max_degree_in < degree_in_node_i:
                max_degree_in = degree_in_node_i
                highest_degree_node = i
        return highest_degree_node

    def __str__(self):
        repr = ""
        for adj in self.adj_list:
            repr += str(adj) + "\n"
        return repr
