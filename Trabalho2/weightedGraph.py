from typing import Tuple, Optional
import heapq


class WeightedGraph:
    def __init__(self, node_count: int = 0, count_edges: int = 0, adj_list: Optional[dict[str, dict[str, int]]] = None) -> None:
        self.node_count = node_count  # número de nós
        self.count_edges = count_edges  # número de arestas
        self.adj_list = adj_list if adj_list is not None else {}  # lista de adjacência

    def add_node(self, node_name: str) -> None:
        node_name = node_name.strip()
        if node_name not in self.adj_list:
            self.adj_list[node_name] = {}
            self.node_count += 1

    def add_directed_edge(self, u: str, v: str, w: int):
        u = u.strip()
        v = v.strip()
        if u not in self.adj_list:
            self.adj_list[u] = {}
        if v not in self.adj_list[u]:
            self.adj_list[u][v] = w
        self.count_edges += 1

    def dijkstra_max_path(self) -> Tuple[int, list[str]]:
        # Define a distância máxima para cada nó como negativa infinita, exceto para o nó "s", cuja distância é zero
        distances = {node: float('-inf') for node in self.adj_list}
        distances['s'] = 0

        # Inicializa a heap com o nó "s"
        heap = [(-distances['s'], 's')]

        # Define o dicionário de predecessores
        predecessors = {node: None for node in self.adj_list}

        # Realiza a busca do caminho máximo com Dijkstra
        while heap:
            (distance, current_node) = heapq.heappop(heap)
            distance = -distance
            for neighbor, weight in self.adj_list[current_node].items():
                new_distance = distance + weight
                if new_distance > distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(heap, (-new_distance, neighbor))

        # Obtém o caminho máximo a partir dos predecessores
        max_path = ['t']
        current_node = 't'
        while predecessors[current_node] is not None:
            max_path.append(predecessors[current_node])
            current_node = predecessors[current_node]
        max_path.reverse()

        return distances['t'], max_path
