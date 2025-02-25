import heapq

from Graph.AdjacencyMatrix import Graph
from Graph.AdjacencyMatrix import GraphType

class BellmanFordAlgorithm:
    def __init__(self, graph:Graph):
        self.graph = graph

    def run(self, source):
        I = float("inf")
        distance = [I]*self.graph.vertex_count()
        path = [-1]*self.graph.vertex_count()
        distance[source] = 0
        for i in range(self.graph.vertex_count() - 1):
            for (u,v,w) in self.graph.get_edges():
                # if distance[u]!=I and distance[u] + w < distance[v]:
                #     distance[v] = distance[u] + w
                #     path[v] = u
                distance[v] = min(distance[u] + w, distance[v])
                path[v] = u

        for (u,v,w) in self.graph.get_edges():
            if distance[u]!=I and distance[u] + w < distance[v]:
                print("Negative cycle exists.")
                return None,None

        return distance, path

    def print_shortest_path(self, source, distance, path):
        for i,item in enumerate (distance):
            # print(f"The distance of vertex {source} -> {i} is {item} and the path is {get_path(path, i)}")
            print(f"The distance of vertex {source} -> {i} is {item}")

    def get_path(self, path, vertex):
        if vertex < 0:
            return []
        return self.get_path(path, path[vertex]) + [vertex]

if __name__ == '__main__':
    graph = Graph(5, GraphType.DIRECTED, True)
    graph.insert_edge(0,1,-1)
    graph.insert_edge(0,2, 4)
    graph.insert_edge(1, 2, 3)
    graph.insert_edge(1, 3, 2)
    graph.insert_edge(1, 4, 2)
    graph.insert_edge(3,1,1)
    graph.insert_edge(4,3,-3)

    bellman_ford_algorithm = BellmanFordAlgorithm(graph)

    print(graph.adjacency_matrix)
    distance, path = bellman_ford_algorithm.run(0)
    if distance is not None:
        print(path)
        bellman_ford_algorithm.print_shortest_path(0,distance, path)