import pandas as pd
import time


class Graph:
    def __init__(self, i: int = 0, j: int = 0, count_nodes: int = 0, count_edges: int = 0, adj_list=None) -> None:
        if adj_list is None:
            adj_list = {}
        self.count_nodes = count_nodes
        self.count_edges = count_edges
        self.adj_list = adj_list
        self.i = i
        self.j = j

        if not adj_list:
            for i in range(self.i):
                for j in range(self.j):
                    adj_list[i, j] = []

    def add_directed_edge(self, a: tuple, arg2: tuple):
        self.adj_list[a].append(arg2)
        self.count_edges += 2

    def depth_search(self, start: tuple, end: tuple):
        desc = {}
        for i in self.adj_list:
            desc[i] = 0
        S = [start]
        R = [start]
        desc[start] = 1
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if desempilhar:
                S.pop()
        return R


def create_graph(arq):
    start_time = time.time()

    with open(arq) as test:
        maze = []
        for line in test:
            maze.append([i for i in line.strip("\n")])
        df = pd.DataFrame(maze)
        print(df)

    g1 = Graph(len(df.axes[0]), len(df.axes[1]))

    for i in range(len(maze)):
        print(i)
        for j in range(len(maze[i])):
            if maze[i][j] == "#":
                g1.adj_list.pop((i, j))
            else:
                if maze[i][j] == "S":
                    start_lab = (i, j)
                if maze[i][j] == "E":
                    end_lab = (i, j)
                if i != 0:
                    if maze[i - 1][j] != "#":
                        g1.add_directed_edge((i, j), (i - 1, j))
                if j != len(maze[i]) - 1:
                    if maze[i][j + 1] != "#":
                        g1.add_directed_edge((i, j), (i, j + 1))
                if i != len(maze) - 1:
                    if maze[i + 1][j] != "#":
                        g1.add_directed_edge((i, j), (i + 1, j))
                if j != 0:
                    if maze[i][j - 1] != "#":
                        g1.add_directed_edge((i, j), (i, j - 1))
    return g1, start_lab, end_lab


