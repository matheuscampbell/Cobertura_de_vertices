import time

# Programa Python3 para imprimir o Vertex Cover
# de um dado grafo não direcionado
from collections import defaultdict
import plotly.graph_objects as go

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

    # Função auxiliar para verificar se um vértice é coberto
    def isCovered(self, vertex, cover):
        for u, v in cover:
            if vertex == u or vertex == v:
                return True
        return False

    # Função para imprimir o Vertex Cover
    def printVertexCover(self):
        
        # Contadores de iterações e tempo
        iterations = 0
        start_time = time.time()
        
        # Gera todas as possíveis combinações de vértices
        # e verifica se elas formam um Vertex Cover válido
        for i in range(1, self.V + 1):
            cover = []
            for u in range(self.V):
                for v in self.graph[u]:
                    iterations += 1
                    if not self.isCovered(u, cover) and not self.isCovered(v, cover):
                        cover.append((u, v))
                        break

            # Verifica se o conjunto de vértices forma um Vertex Cover
            if len(cover) == i:
                # Imprime o vertex cover
                for vertex in range(self.V):
                    if self.isCovered(vertex, cover):
                        #print(vertex, end=' ')
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
    sizes = [10, 100, 750, 1500]
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