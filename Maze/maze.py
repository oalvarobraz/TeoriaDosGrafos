import pandas as pd
import timeit
from graph import Graph


def create_graph(arq):
    start_time = timeit.default_timer()

    with open(arq) as test:
        maze = []
        for line in test:
            maze.append([i for i in line.strip("\n")])
        df = pd.DataFrame(maze)

    g1 = Graph(len(df.axes[0]), len(df.axes[1]))

    for i in range(len(maze)):
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

    end_time = timeit.default_timer()

    execution_time = (end_time - start_time)

    return df, g1, start_lab, end_lab, execution_time


op = '1'
while op != '0':
    op = str(input("Informe o nome do arquivo (0 para sair) "))
    if op != '0':
        maze, g1, start, end, execution_time = create_graph(op)
        print("|| IMPRIMINDO LABBIRINTO ||")
        print(maze)
        print(f"\n|| Caminho: {g1.depth_search(start, end)}")
        print(f"|| Tempo: {execution_time}")
