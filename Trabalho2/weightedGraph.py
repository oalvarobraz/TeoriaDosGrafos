import pandas as pd
from weightedGraph import WeightedGraph
import os


def msg_error():
    print("|| Possíveis erros:")
    print("-> Arquivo não esta na pasta critical_path")
    print("-> Nome do arquivo escrito de forma incorreta")


def create_graph(nome_arquivo):
    filename, extension = os.path.splitext(nome_arquivo)
    if extension == ".xlsx":
        try:
            arq = pd.read_excel("critical_path/" + nome_arquivo)
        except FileNotFoundError:
            return None
    elif extension == ".csv":
        try:
            arq = pd.read_csv("critical_path/" + nome_arquivo)
        except FileNotFoundError:
            return None
    else:
        return None

    graph = WeightedGraph()
    graph.add_node("s")
    # Adicionando todas as arestas dos nos para t
    for linha in arq.index:
        graph.add_directed_edge(arq["Código"][linha], "t", arq["Duração"][linha])
    graph.add_node("t")

    # Adicionando as arestas iniciais de s para os códigos que não tem dependencia
    for linha in arq.index:
        if pd.isna(arq["Dependências"][linha]):
            graph.add_directed_edge("s", arq["Código"][linha], 0)

    # Adicionando as arestas de dependência
    for linha in arq.index:
        if not pd.isna(arq["Dependências"][linha]):
            dependencias = arq["Dependências"][linha].split(';')
            for dependencia in dependencias:
                if dependencia != 'nan':
                    graph.add_directed_edge(dependencia, arq["Código"][linha], arq["Duração"][linha])

    return graph, arq


# Calculando o caminho máximo e imprimindo para o usuário as materias que compoem e o tempo mónimo
def max_path(graph: WeightedGraph, arq):
    temp, dj_max_path = graph.dijkstra_max_path()

    print("Caminho Crítico:")
    for i in dj_max_path:
        if any(char.isdigit() for char in i):
            vish = arq.loc[arq["Código"] == i]
            if not vish.empty:
                print(f" - {vish['Nome'].values[0]}")
    print(f"Tempo Mínimo: {temp}")


op = '1'
while op != '0':
    op = str(input("\n|| Informe o nome do arquivo (0 para sair): critical_path/"))
    if op != '0':
        name, exten = os.path.splitext(op)
        if exten == ".xlsx" or exten == ".csv":
            print("\nProcessando...")
            if create_graph(op) is not None:
                g1, arquivo = create_graph(op)
                max_path(g1, arquivo)
            else:
                print("\nArquivo não encontrado")
                msg_error()
        else:
            print("Formato não suportado! ")
            msg_error()
    os.system('cls')
