from graph import Graph

# Criando o grafo
g1 = Graph(4)
# Adicionando as arestas
g1.add_directed_edge(1, 0)
g1.add_directed_edge(0, 2)
g1.add_directed_edge(2, 0)
g1.add_directed_edge(0, 3)
g1.add_directed_edge(3, 2)
# Imprimindo o grafo
print('GRAPH 1:', g1.adj_list)
# Imprimindo o grau de saída do nó 0
print("DEGREE_OUT(0):", g1.degree_out(0))
# Imprimindo o grau de saída do nó 1
print("DEGREE_OUT(1):", g1.degree_out(1))
#  Imprimindo qual é o nó que tem maior grau
print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
# Imprimindo o grau de entrada do nó 0
print("DEGREE_IN(0):", g1.degree_in(0))
# Imprimindo o grau de entrada do nó 1
print("DEGREE_IN(1):", g1.degree_in(1))
