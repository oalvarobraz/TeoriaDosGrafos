import pandas as pd
from Graph import Graph
import timeit
import os


def create_graph(arq):
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

    return df, g1, start_lab, end_lab


def show_walk(graph, start, end):
    for i in graph.depth_search(start, end):
        maze[i[1]][i[0]] = '.'
    print(pd.DataFrame(maze))

    df = pd.DataFrame(maze)
    with open("result.txt", 'w') as f:
        dfAsString = df.to_string(header=False, index=False)
        f.write(dfAsString)


op = '1'
while op != '0':
    op = str(input("Informe o nome do arquivo (0 para sair) "))
    if op != '0':
        maze, g1, start, end = create_graph(op)
        start_time = timeit.default_timer()
        walk = g1.depth_search(start, end)
        execution_time = float('%g' % (timeit.default_timer() - start_time))
        print("|| IMPRIMINDO LABBIRINTO ||")
        print(maze)
        print(f"\n|| Caminho: {walk}")
        print(f"|| Tempo: {execution_time}")

        show_walk(g1, start, end)
        os.system("PAUSE")
        os.system('cls')
