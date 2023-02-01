import pandas as pd
from graph import Graph
import timeit
import os


def create_graph(arq):
    with open("mazes/"+arq) as test:
        make_maze = []
        for line in test:
            make_maze.append([i for i in line.strip("\n")])
        df = pd.DataFrame(make_maze)

    graph = Graph(len(df.axes[0]), len(df.axes[1]))

    for i in range(len(make_maze)):
        for j in range(len(make_maze[i])):
            if make_maze[i][j] == "#":
                graph.adj_list.pop((i, j))
            else:
                if make_maze[i][j] == "S":
                    sl = (i, j)
                if make_maze[i][j] == "E":
                    el = (i, j)
                if i != 0:
                    if make_maze[i - 1][j] != "#":
                        graph.add_directed_edge((i, j), (i - 1, j))
                if j != len(make_maze[i]) - 1:
                    if make_maze[i][j + 1] != "#":
                        graph.add_directed_edge((i, j), (i, j + 1))
                if i != len(make_maze) - 1:
                    if make_maze[i + 1][j] != "#":
                        graph.add_directed_edge((i, j), (i + 1, j))
                if j != 0:
                    if make_maze[i][j - 1] != "#":
                        graph.add_directed_edge((i, j), (i, j - 1))

    return df, graph, sl, el


def show_walk(graph, start, end):
    for i in graph.depth_search(start, end):
        maze[i[1]][i[0]] = '.'
    print(pd.DataFrame(maze))

    df = pd.DataFrame(maze)
    with open("result.txt", 'w') as f:
        df_to_string = df.to_string(header=False, index=False)
        f.write(df_to_string)


op = '1'
while op != '0':
    op = str(input("|| Informe o nome do arquivo (0 para sair): mazes/"))
    if op != '0':
        maze, g1, start, end = create_graph(op)
        start_time = timeit.default_timer()
        walk = g1.depth_search(start, end)
        execution_time = float('%g' % (timeit.default_timer() - start_time))
        print(f"|| Caminho: {walk}")
        print(f"|| Tempo: {execution_time}")
        print("|| O caminho está em result.txt \n")
        os.system("PAUSE")
        os.system('cls') or None
