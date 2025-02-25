from operator import truediv


class Graph:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.adjacency_matrix = [[0]*num_vertex for _ in range(num_vertex)]

    def add_edge(self, from_vertex, to_vertex):
        self.adjacency_matrix[from_vertex][to_vertex] = 1

        # # 1,2,3,4,5
        # [[0,1,0,0,0], #1
        #  [0,0,0,0,0], #2
        #  [0,0,0,1,0], #3
        #  [0,0,0,0,0], #4
        #  [0,0,0,0,0]] #5

    def dfs(self, node, graph, visited, on_stack, order):
        visited[node] = True
        on_stack[node] = True

        for i in range(graph.num_vertex):
            if graph.adjacency_matrix[node][i] == 1:
                if not visited[i]:
                    if not self.dfs(i, graph, visited, on_stack, order):
                        return False
                    elif on_stack[i]:
                        return False

        on_stack[node] = False
        order.append(node)

        return True

    def topological_sort(self, graph):
        visited = [False]*graph.num_vertex
        on_stack = [False]*graph.num_vertex
        order = []

        for i in range(graph.num_vertex):
            if not visited[i]:
                if not self.dfs(i,graph, visited, on_stack, order):
                    return None

        return order[::-1]

if __name__  ==  "__main__":''
    num_vertex = 8
    edges = [[7,5],[7,6],[5,4],[6,4],[5,2],[6,3],[2,1],[3,1],[1,0]]
    graph = Graph(num_vertex)
    for u,v in edges:
        graph.add_edge(u,v)
    result = graph.topological_sort(graph)
    print("Topological Sort: ", result)