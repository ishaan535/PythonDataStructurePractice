import heapq

from Graph.AdjacencyMatrix import Graph
from Graph.GraphType import GraphType

I = float("inf")

class DijkstraAlgorithm:
    def __init__(self, graph:Graph):
        self.graph = graph

    def run(self, start_vertex):
        if start_vertex not in self.graph.vertices:
            raise ValueError("Start vertex is not in the Graph.")
        distance_list = [I]*self.graph.vertex_count()
        start_vertex_index = self.graph.vertices.index(start_vertex)
        # print(distance_list)
        path_list = [None]*self.graph.vertex_count()
        distance_list[start_vertex_index] = 0
        path_list[start_vertex_index] = start_vertex_index
        priority_queue = [(0, start_vertex_index)]
        while priority_queue:
            current_distance,current_vertex = heapq.heappop(priority_queue)
            if current_distance > distance_list[current_vertex]:
                continue
            for neighbour, weight in self.graph.get_neighbor_nodes(current_vertex):
                distance = current_distance + weight
                if distance < distance_list[neighbour]:
                    distance_list[neighbour] = distance
                    heapq.heappush(priority_queue, (distance, neighbour))
                    path_list[neighbour] = current_vertex


        for i, distance in enumerate(distance_list):
            print(f"Distance from {self.graph.vertices[start_vertex_index]} to {self.graph.vertices[i]}: {distance}")



if __name__  ==  "__main__":
    num_vertex = 6
    graph = Graph(6,GraphType.DIRECTED,True,vertices=['A','B','C','D','E','F'])
    graph.insert_edge("A", "B", 7)
    graph.insert_edge("A", "C", 12)
    graph.insert_edge("B", "C", 2)
    graph.insert_edge("B", "D", 9)
    graph.insert_edge("C", "E", 10)
    graph.insert_edge("E", "D", 4)
    graph.insert_edge("E", "F", 5)
    graph.insert_edge("D", "F", 1)

    dijkstra = DijkstraAlgorithm(graph)
    dijkstra.run("A")

    # print(graph.adjacency_list)
    # print(graph.all_edges)