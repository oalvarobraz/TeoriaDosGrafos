from weightedGraph import WeightedGraph
import time

# Metodo de criar um grafo ponderado na mão

# g2 = WeightedGraph(5)
# g2.add_directed_edge(0, 1, 6)  # no origem, no destino, peso
# g2.add_directed_edge(0, 2, 2)
# g2.add_directed_edge(1, 2, 3)
# g2.add_directed_edge(1, 3, 1)
# g2.add_directed_edge(1, 4, 3)
# g2.add_directed_edge(2, 1, 2)
# g2.add_directed_edge(2, 3, 5)
# g2.add_directed_edge(3, 4, 3)


# Metodo de criar um grafo ponderado lendo um arquivo txt

# g3 = WeightedGraph(5)
# g3.read_file("datasets/shortestPath/rome99c.txt")
#
# start_time = time.time()
# g3.bellmand_ford(0)
# print(f"Tempo Bellmand Ford: {time.time() - start_time}")
#
# start_time = time.time()
# g3.bellmand_ford_better(0)
# print(f"Tempo Bellmand Ford Melhorado: {time.time() - start_time}")

g1 = WeightedGraph()
g1.read_file("datasets/shortestPath/USA-road-dt.NY.txt")

start_time = time.time()
print(g1.dijkstra_fila_prior(0))
print(f"Tempo Dijstra prioridade: {time.time() - start_time}")





# g4 = WeightedGraph(4)
# g4.add_directed_edge(0, 1, 6)
# g4.add_directed_edge(1, 0, 3)
# g4.add_directed_edge(1, 2, 7)
# g4.add_directed_edge(2, 1, 2)
# g4.add_directed_edge(0, 2, 2)
# g4.add_directed_edge(1, 3, 5)
# g4.add_directed_edge(2, 3, 1)
# g4.add_directed_edge(3, 2, 4)
#
# print(g4.floyd_warshall())

#g5 = WeightedGraph()
#g5.read_file("datasets/shortestPath/USA-road-dt.NY.txt")

#print(g5.bellmand_ford_better(0))
