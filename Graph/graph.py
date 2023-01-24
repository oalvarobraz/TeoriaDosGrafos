class Graph:

    def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list=None) -> None:
        if adj_list is None:
            adj_list = []
        self.count_nodes = count_nodes  # numero de nos
        self.count_edges = count_edges  # numero de arestas
        self.adj_list = adj_list  # lista de adjacencia

        if not adj_list:
            for _ in range(self.count_nodes):
                adj_list.append([])
                # Quando não vamos utilizar o indice dentro do laço usualmente colocamos _
        # Se a lista de adjacencia estiver vazia, o algoritmo vai criar uma lista de listas vazias
        # demonstração: adj_list = [[], [], [], []]

    # realizar o tratamento caso usuario tente adicionar um nos(u) que não esteja dentro do intervajo de [0,count_node]

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= self.count_nodes or v < 0 or v >= self.count_nodes:
            print(f'Edge ({u},{v}) could not be added because one of the values is out of the allowed range (0,'
                  f'{self.count_nodes - 1})')
        else:
            self.adj_list[u].append(v)
            self.count_edges += 1

    def add_undirected_edge(self, u: int, v: int):
        # Não é a meljor solução pq estou repetindo um codigo ja utilizado
        # if u < 0 or u >= self.count_nodes or v < 0 or v >= self.count_nodes:
        #     print(f'Edge ({u},{v}) could not be added because one of the values is out of the allowed range (0,'
        #           f'{self.count_nodes -1})')
        # else:
        #     self.adj_list[u].append(v)
        #     self.adj_list[v].append(u)
        #     self.count_edges += 2
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def add_node(self):
        self.adj_list.append([])
        self.count_nodes += 1

    def degree_out(self, u: int) -> int:  # função que retorna o grau de saida do no, depois validar e criar uma função
        # de validação
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        count = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                count += 1
        # for i in range(len(self.adj_list)):
        #     for j in range(len(self.adj_list[i])):
        #         if self.adj_list[i][j] == u:
        #             count += 1
        return count

    def highest_degree_out(self) -> int:  # função que rotarna o nó de maior grau de saida
        mode = 0
        max_degree_out = 0
        for i in range(self.count_nodes):
            if self.degree_out(i) > max_degree_out:
                max_degree_out = self.degree_out(i)
                mode = i
        return mode

    def highest_degree_in(self) -> int:  # função que retorna o nó com o maior grau de entrada
        max_degree_in = float("inf")
        highest_degree_node = 0
        for i in range(self.count_nodes):
            degree_in_node_i = self.degree_in(i)
            if max_degree_in < degree_in_node_i:
                max_degree_in = degree_in_node_i
                highest_degree_node = i
        return highest_degree_node

    # def is_complete(self) -> int:
    #     """
    #     Returns whether the graph is complete
    #
    #     :return: 0: ins´t complete
    #              1: is complete
    #
    #     """
    #     max_degree_out = self.count_nodes - 1
    #     complete = 0
    #     for i in range(self.count_nodes):
    #         if self.degree_out(i) >= max_degree_out:
    #             complete = 1
    #         else:
    #             complete = 0
    #     return complete

    def complete(self):
        """
            Calculetes the density
        :return: self.node_count*(self.node_count - 1) == self.edge_count
        """
        # return self.density() == 1
        return self.count_nodes * (self.count_nodes - 1) == self.count_edges

    def density(self):
        return self.count_edges / (self.count_nodes * (self.count_nodes - 1))

    def regular(self):
        for i in range(1, self.count_nodes):
            if self.degree_out(i) != self.degree_out(0):
                return False
        return True

    def complement(self, g2):
        """Returns the complent of a graph"""
        for i in range(len(self.adj_list)):
            for j in range(len(self.adj_list)):
                if j not in self.adj_list[i] and j != i and j not in g2.adj_list[i]:
                    g2.add_undirected_edge(i, j)
        return g2

    def subgraph(self, g2):
        """Returns True iif g2 is a subgraph of self"""
        for i in range(len(g2.adj_list)):
            for j in range(len(g2.adj_list[i])):
                if j not in self.adj_list[i]:
                    return False
        return True

    def passeio(self, passeio: list):
        for i in range(len(passeio)-1):
            if not self.adj_list[passeio[i]].__contains__(passeio[i+1]):
                return False
        return True

    def trilha(self, trilha: list):
        verifica = []
        for i in range(len(trilha)-1):
            if not self.adj_list[trilha[i]].__contains__(trilha[i+1]):
                return False
            else:
                if verifica.__contains__([trilha[i], trilha[i + 1]]) or verifica.__contains__([trilha[i + 1], trilha[i]]):
                    return False
            trilha_aux = [trilha[i], trilha[i+1]]
            verifica.append(trilha_aux)
        return True

    def circuito(self, circuito: list):
        if circuito[0] != circuito[len(circuito)-1]:
            return False
        else:
            return self.trilha(circuito)

    def verifica(self, percurso):
        verifica = []
        verifica2 = []
        for i in range(len(percurso) - 1):
            if not self.adj_list[percurso[i]].__contains__(percurso[i + 1]):
                return False
            else:
                if verifica.__contains__([percurso[i], percurso[i + 1]]) or verifica.__contains__(
                        [percurso[i + 1], percurso[i]]) or verifica2.__contains__(percurso[i]):
                    return False
            verifica.append([percurso[i], percurso[i + 1]])
            verifica2.append(percurso[i])
        return True

    def caminho(self, caminho: list):
        if caminho[0] != caminho[len(caminho)-1]:
            return self.verifica(caminho)
        return False

    def ciclo(self, ciclo: list):
        if ciclo[0] == ciclo[len(ciclo) - 1]:
            return self.verifica(ciclo)
        else:
            return False
