class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
        self.all_edges = []

    def add_edge(self, source, destination):
        edge = Edge(source, destination)
        self.adjacency_list[source].insert(0,edge)
        self.all_edges.append(edge)

    def make_set(self, parent):
        for i in range(self.num_vertices):
            parent[i] = i

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            return self.find(parent, parent[vertex])
        return vertex

    def union(self, parent, x, y):
        x_Parent = self.find(parent, x)
        y_Parent = self.find(parent, y)
        parent[y_Parent] = x_Parent

    def is_cycle_exists(self):
        parent = [0]*self.num_vertices
        self.make_set(parent)
        for edge in self.all_edges:
            x_source = self.find(parent, edge.source)
            x_destination = self.find(parent, edge.destination)
            if x_source == x_destination:
                return True
            else:
                self.union(parent, x_source, x_destination)
        return False

if __name__  ==  "__main__":
    graph = Graph(6)
    graph.add_edge(0,1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    # graph.add_edge(5, 2)
    print(graph.is_cycle_exists())