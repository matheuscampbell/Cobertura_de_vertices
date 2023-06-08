import time
from collections import defaultdict
import plotly.graph_objects as go

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printVertexCover(self):
        visited = [False] * self.V
        iterations = 0
        start_time = time.time()

        u = 0
        while u < self.V:  # Loop para percorrer todos os vértices do grafo
            if not visited[u]:
                v_index = 0
                while v_index < len(self.graph[u]):  # Loop para percorrer todos os adjacentes de u
                    iterations += 1
                    v = self.graph[u][v_index]
                    if not visited[v]:  # Verifica se o vértice v ainda não foi visitado
                        visited[v] = True
                        visited[u] = True
                        break  # Interrompe o loop quando encontra uma aresta válida (u, v)
                    v_index += 1
            u += 1

        for j in range(self.V):
            if visited[j]:
                pass

        print()

        end_time = time.time()
        print("Tempo de execução:", end_time - start_time, "segundos")
        print("Quantidade de iterações:", iterations)
        return (end_time - start_time, iterations)


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