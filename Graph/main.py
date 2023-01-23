from graph import Graph


def busca_largura(G: Graph, s):
    desc = [0 for i in range(G.count_nodes)]
    Q = [s]
    R = [s]
    desc[s] = 1
    while len(Q) != 0:
        u = Q.pop(0)
        for v in G.adj_list[u]:
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
    return R


def busca_profundidade(G: Graph, s):
    desc = [0 for i in range(G.count_nodes)]
    S = [s]
    R = [s]
    desc[s] = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in G.adj_list[u]:
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
        if desempilhar:
            S.pop()
    return R


g1 = Graph(10)
g1.add_undirected_edge(0, 3)
g1.add_undirected_edge(0, 4)
g1.add_undirected_edge(0, 5)
g1.add_undirected_edge(5, 6)
g1.add_undirected_edge(5, 8)
g1.add_undirected_edge(5, 7)
g1.add_undirected_edge(7, 9)
g1.add_undirected_edge(9, 8)
g1.add_undirected_edge(1, 2)
print(g1.adj_list)

valor = busca_largura(g1, 2)
print(valor)


# # Criando o grafo
# g1 = Graph(3)
# # Adicionando as arestas
# g1.add_undirected_edge(0, 1)
# g1.add_undirected_edge(0, 2)
# g1.add_undirected_edge(1, 2)
#
# # Imprimindo o grafo
# print('GRAPH 1:', g1.adj_list)
# # Imprimindo o grau de saída do nó 0
# print("DEGREE_OUT(0):", g1.degree_out(0))
# # Imprimindo o grau de saída do nó 1
# print("DEGREE_OUT(1):", g1.degree_out(1))
# #  Imprimindo qual é o nó que tem maior grau
# print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
# # Imprimindo o grau de entrada do nó 0
# print("DEGREE_IN(0):", g1.degree_in(0))
# # Imprimindo o grau de entrada do nó 1
# print("DEGREE_IN(1):", g1.degree_in(1))
#
# print('IS COMPLET: ', g1.is_complete())
#
# # Criando outro grafo
# g2 = Graph(3)
# g2.add_directed_edge(0, 1)
# g2.add_directed_edge(0, 2)
# g2.add_undirected_edge(2, 1)
#
# print('GRAPH 2:', g2.adj_list)
# print('IS COMPLET: ', g2.is_complete())
