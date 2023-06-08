import time
import plotly.graph_objects as go
# Programa Python3 para imprimir o Vertex Cover
# de um dado grafo não direcionado
from collections import defaultdict


# Esta classe representa um grafo direcionado
# usando uma representação de lista de adjacência
class Graph:

    def __init__(self, vertices):

        # Número de vértices
        self.V = vertices

        # Dicionário padrão para armazenar o grafo
        self.graph = defaultdict(list)

    # Função para adicionar uma aresta ao grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Função para imprimir o Vertex Cover
    def printVertexCover(self):

        # Inicializa todos os vértices como não visitados.
        visited = [False] * (self.V)

        # Contadores de iterações e tempo
        iterations = 0
        start_time = time.time()

        # Considere todas as arestas uma por uma
        for u in range(self.V):
            # Uma aresta só é escolhida quando
            # visited[u] e visited[v]
            # são falsos
            if not visited[u]:
                # Percorre todos os adjacentes de u e
                # escolhe o primeiro vértice ainda não visitado
                # (Basicamente estamos escolhendo
                # uma aresta (u, v) entre as arestas restantes.
                for v in self.graph[u]:
                    iterations += 1
                    if not visited[v]:
                        # Adiciona os vértices (u, v) ao
                        # conjunto de resultados. Fazemos o vértice
                        # u e v visitado para que todas as
                        # arestas entre eles sejam ignoradas
                        visited[v] = True
                        visited[u] = True
                        break

        # Imprime o vertex cover
        for j in range(self.V):
            if visited[j]:
                # print(j, end=' ')
                pass

        print()

        # Tempo de execução e quantidade de iterações
        end_time = time.time()
        print("Tempo de execução:", end_time - start_time, "segundos")
        print("Quantidade de iterações:", iterations)
        return (end_time - start_time, iterations)


# Código do programa
def run_tester(n):
    # Cria um grafo conforme
    # o diagrama acima
    TAMANHO_GRAFO = n
    g = Graph(TAMANHO_GRAFO)
    for i in range(0, TAMANHO_GRAFO):
        g.addEdge(i, i + 1)

    return g.printVertexCover()


def generate_graph():
    sizes = [10, 100, 1000, 2000, 10000, 50000, 100000]
    times = []
    iterations = []

    for size in sizes:
        print("Tamanho do grafo:", size)
        [tempo, iteracoes] = run_tester(size)
        print("tempo:", tempo)
        print("iteracoes:", iteracoes)
        times.append(tempo)
        iterations.append(iteracoes)
        print()

    # Cria o gráfico de linhas interativo
    fig = go.Figure()

    # Adiciona as linhas para tempo e iterações
    fig.add_trace(go.Scatter(x=sizes, y=times, mode='lines+markers', name='Tempo'))
    fig.add_trace(go.Scatter(x=sizes, y=iterations, mode='lines+markers', name='Iterações'))
    fig.add_trace(go.Scatter(x=times, y=iterations, mode='lines+markers', name='Iterações/Tempo'))

    # Personaliza o layout do gráfico
    fig.update_layout(title='Comparação de tempo e iterações',
                      xaxis_title='Tempo',
                      yaxis_title='Iterações')

    # Exibe o gráfico interativo
    fig.show()


if __name__ == '__main__':
    generate_graph()
