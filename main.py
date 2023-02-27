from weightedGraph import WeightedGraph
import time

# Metodo de criar um grafo ponderado na mão

g1 = WeightedGraph()
g1.read_file("datasets/shortestPath/USA-road-dt.NY.txt")

start_time = time.time()
print(g1.dijkstra_fila_prior(0))
print(f"Tempo Dijstra prioridade: {time.time() - start_time}")
