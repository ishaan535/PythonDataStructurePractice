from Graph.AdjacencyMatrix import Graph
from Graph.GraphType import GraphType

class KruskalAlgorithm:
    def __init__(self, graph:Graph):
        self.graph = graph

    def get_unique_edges(self):
        edge_list = self.graph.get_edges()
        seen_edges = set()
        unique_edges = []

        for edge in edge_list:
            u,v,w = edge
            if (v,u,w) not in seen_edges:
                unique_edges.append(edge)
                seen_edges.add(edge)

        return unique_edges

    def make_set(self, parent):
        for i in range(self.graph.vertex_count()):
            parent[i] = i

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            return self.find(parent, parent[vertex])
        return vertex

    def union(self, parent, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)
        parent[y_parent] = x_parent

    def is_cycle_exists(self):
        parent = [0]*self.graph.vertex_count()
        self.make_set(parent)
        for u,v,w in self.get_unique_edges():
            x_source = self.find(parent, u)
            x_destination = self.find(parent, v)
            if x_source == x_destination:
                return True
            else:
                self.union(parent, x_source, x_destination)
        return False

    def mst(self):
        sorted_edges = sorted(self.get_unique_edges(), key = lambda x: x[2])
        parent = [i for i in range(self.graph.vertex_count())]
        mst = []
        number_edge = 0
        while number_edge < self.graph.vertex_count() - 1:
            edge = sorted_edges.pop(0)
            x_set = self.find(parent, edge[0])
            y_set = self.find(parent, edge[1])
            if x_set == y_set:
                continue
            else:
                mst.append(edge)
                number_edge += 1
                self.union(parent, x_set, y_set)
        print("Minimum Spanning Tree: ")

        for index,edge in enumerate(mst):
            print(f"edge-{index} source:{edge[0]} destination:{edge[1]} weight:{edge[2]}")


if __name__  ==  "__main__":
    graph = Graph(6, GraphType.UNDIRECTED, True)
    graph.insert_edge(0,1,4)
    graph.insert_edge(0,2,3)
    graph.insert_edge(1,2,1)
    graph.insert_edge(1,3,2)
    graph.insert_edge(2,3,4)
    graph.insert_edge(3,4,2)
    graph.insert_edge(4,5,6)
    kruskal_algorithm = KruskalAlgorithm(graph)
    kruskal_algorithm.mst()
    #print(kruskal_algorithm.get_unique_edges())

