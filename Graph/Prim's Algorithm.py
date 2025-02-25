from operator import truediv

from Graph.AdjacencyMatrix import Graph
from Graph.GraphType import GraphType

INF = float("inf")

class PrimsAlgorithm:
    def __init__(self, graph:Graph):
        self.graph = graph

    def mst(self):
        visited = [0] * self.graph.vertex_count()
        visited[0] = True
        no_edge = 0
        while no_edge < self.graph.vertex_count() - 1:
            min = INF
            x = 0
            y = 0
            for i in range(self.graph.vertex_count()):
                if visited[i]:
                    for j in range(self.graph.vertex_count()):
                        if (not visited[j]) and self.graph.adjacency_matrix[i][j]:
                            if min > self.graph.adjacency_matrix[i][j]:
                                min = self.graph.adjacency_matrix[i][j]

                                x = i
                                y = j

            print(str(x) + "-" + str(y) + ":" + str(self.graph.adjacency_matrix[x][y]))
            visited[y] = True
            no_edge += 1



if __name__  ==  "__main__":
    graph = Graph(6, GraphType.UNDIRECTED, True)
    graph.insert_edge(0,1,4)
    graph.insert_edge(0,2,3)
    graph.insert_edge(1,2,1)
    graph.insert_edge(1,3,2)
    graph.insert_edge(2,3,4)
    graph.insert_edge(3,4,2)
    graph.insert_edge(4,5,6)
    prims_algorithm = PrimsAlgorithm(graph)
    prims_algorithm.mst()