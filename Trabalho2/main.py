import pandas as pd
from weightedGraph import WeightedGraph
import os


def create_graph(nome_arquivo):
    filename, extension = os.path.splitext(nome_arquivo)
    if extension == ".xlsx":
        arq = pd.read_excel("critical_path/" + nome_arquivo)
    elif extension == ".csv":
        arq = pd.read_csv("critical_path/" + nome_arquivo)
    else:
        print("Formato não suportado!")
        return None

    g2 = WeightedGraph()
    g2.add_node("s")
    # Adicionando todas as arestas dos nos para t
    for linha in arq.index:
        codigos = arq["Código"][linha].split(';')
        for codigo in codigos:
            if codigo != 'nan':
                g2.add_directed_edge(codigo, "t", arq["Duração"][linha])
    g2.add_node("t")

    # Adicionando as arestas iniciais de s para os códigos que não tem dependencia
    for linha in arq.index:
        if pd.isna(arq["Dependências"][linha]):
            g2.add_directed_edge("s", arq["Código"][linha], 0)

    # Adicionando as arestas de dependência
    for linha in arq.index:
        if not pd.isna(arq["Dependências"][linha]):
            dependencias = arq["Dependências"][linha].split(';')
            for dependencia in dependencias:
                if dependencia != 'nan':
                    g2.add_directed_edge(dependencia, arq["Código"][linha], arq["Duração"][linha])

    return g2, arq


def max_path(graph: WeightedGraph, arq):
    temp, dj_max_path = graph.dijkstra_max_path()

    print("Caminho Crítico:")
    for i in dj_max_path:
        if any(char.isdigit() for char in i):
            vish = arq.loc[arq["Código"] == i]
            if not vish.empty:
                print(f" - {vish['Nome'].values[0]}")
    print(f" Tempo Mínimo: {temp}")


op = '1'
while op != '0':
    op = str(input("\n|| Informe o nome do arquivo (0 para sair): critical_path/"))
    if op != '0':
        print("Processando...")
        g1, arquivo = create_graph(op)
        max_path(g1, arquivo)
    os.system('cls')
