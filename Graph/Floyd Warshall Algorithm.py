import heapq

from Graph.AdjacencyMatrix import Graph
from Graph.GraphType import GraphType

I = float("inf")

class FloydWarshallAlgorithm:
    def __init__(self, graph:Graph):
        self.graph = graph

    def run(self):
        cost = self.graph.adjacency_matrix
        path = [[None for x in range(self.graph.vertex_count())]for y in range(self.graph.vertex_count())]
        for v in range(self.graph.vertex_count()):
            for u in range(self.graph.vertex_count()):
                if v==u:
                    path[v][u]=0
                elif cost[v][u] != I:
                    path[v][u]=v
                else:
                    path[v][u]=-1
        for k in range(self.graph.vertex_count()):
            for v in range(self.graph.vertex_count()):
                for u in range(self.graph.vertex_count()):
                    if cost[v][k] != I and cost[k][u] != I and cost[v][k]+cost[k][u]<cost[v][u]:
                        cost[v][u] =  cost[v][k] + cost[k][u]
                        path[v][u] = path[k][u]
                if cost[v][v] < 0:
                    print("Negative weight cycle exists.")
                    return

        return cost,path

    def get_path(self, path, v, u, route):
        if path[v][u] == v:
            return
        self.get_path(path,v,path[v][u], route)
        route.append(self.graph.vertices[path[v][u]])

    def print(self, cost, path):
        for v in range(self.graph.vertex_count()):
            for u in range(self.graph.vertex_count()):
                if u != v and path[v][u]!=-1:
                    route = [self.graph.vertices[v]]
                    self.get_path(path,v,u,route)
                    route.append(self.graph.vertices[u])
                    full_path = "->".join(str(x) for x in route)
                    print(f"The shortest path from {self.graph.vertices[v]} -> {self.graph.vertices[u]} is {full_path} with distance {cost[v][u]}")


if __name__ == "__main__":
    graph = Graph(5, GraphType.DIRECTED, True, vertices=[1,2,3,4,5], default_val=I)
    graph.insert_edge(1,2,3)
    graph.insert_edge(1, 3, 8)
    graph.insert_edge(1, 5, -4)
    graph.insert_edge(2, 5, 7)
    graph.insert_edge(2, 4, 1)
    graph.insert_edge(3, 2, 4)
    graph.insert_edge(4, 3, -5)
    graph.insert_edge(4, 1, 2)
    graph.insert_edge(5, 4, 6)

    floydwarshallalgorithm = FloydWarshallAlgorithm(graph)

    cost,path = floydwarshallalgorithm.run()
    floydwarshallalgorithm.print(cost,path)