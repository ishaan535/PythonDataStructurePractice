import sys
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp

from Graph.GraphType import GraphType
from Graph.Vertex import Vertex
from Queues.QueueUsingLL import Queue
from Stacks.StackUsingLinkedList import Stack

# Importing GraphType Enum to specify whether the graph is directed or undirected


# Adding current directory to system path to resolve module imports
sys.path.append('.')



class Graph:
    def __init__(self, vertices_count, graph_type=GraphType.DIRECTED, weighted=False, default_val=0, vertices=None):
        # If no custom vertex names are provided, create default numeric labels
        if vertices is None:
            self.vertices = [i for i in range(vertices_count)]
        else:
            if vertices_count != len(vertices):
                raise ValueError("Vertex count don't match with list of vertex")
            self.vertices = vertices

        self._vertices_count = vertices_count  # Total number of vertices
        self._type = graph_type  # Graph type (Directed or Undirected)
        self._weighted = weighted  # Indicates if the graph is weighted
        self.default_value = default_val  # Default value for edges

        # Initialize adjacency matrix with default values
        self._adjMAT = [[default_val for _ in range(vertices_count)] for _ in range(vertices_count)]

        # Ensure diagonal elements (self-loops) are 0 when a nonzero default value is used
        if default_val != 0:
            self._adjMAT = [[0 if i == j else default_val for j in range(vertices_count)] for i in
                            range(vertices_count)]

        # Visited array to track nodes during traversal
        self._visited = [False] * self._vertices_count
        self._vertex_list = [None] * vertices_count  # Storing the node list so that can be used in AStar Search

    @property
    def adjacency_matrix(self):
        """Returns the adjacency matrix representation of the graph."""
        return self._adjMAT

    @property
    def vertex_list(self):
        return self._vertex_list

    def insert_edge(self, vertex_u, vertex_v, weight=1):

        if vertex_u not in self.vertices or vertex_v not in self.vertices:
            raise ValueError("One or both vertices are not in the graph.")

        # Get indices of the vertices
        u = self.vertices.index(vertex_u)
        v = self.vertices.index(vertex_v)

        # Assign weight (or default value 1 for unweighted graphs)
        self._adjMAT[u][v] = weight

        # If the graph is undirected, add the edge in the opposite direction
        if self._type == GraphType.UNDIRECTED:
            self._adjMAT[v][u] = weight

    def add_vertex(self, vertex, x,y):
        if vertex not in self.vertices :
            raise ValueError("One or both vertices are not in the graph.")
        vertex_index = self.vertices.index(vertex)
        self._vertex_list[vertex_index] = Vertex(x, y, vertex, vertex_index)

    def remove_edge(self, u, v):
        """Removes an edge between two vertices by setting its value to 0."""
        self._adjMAT[u][v] = 0
        if self._type == GraphType.UNDIRECTED:
            self._adjMAT[v][u] = 0

    def exist_edge(self, u, v):
        """Checks if an edge exists between two vertices."""
        return self._adjMAT[u][v] != self.default_value

    def get_edge_weight(self,u,v):
        if self._adjMAT[u][v] != self.default_value:
            return self._adjMAT[u][v]
        else:
            return  None

    def print_edges(self):
        for i in range(self._vertices_count):
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    if self._weighted:
                        print(f'{self.vertices[i]} -- {self.vertices[j]} = {self._adjMAT[i][j]}')
                    else:
                        print(f'{self.vertices[i]} -- {self.vertices[j]}')

    def get_edges(self):
        edge_list = []
        for i in range(self._vertices_count):
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    edge_list.append((i, j, self._adjMAT[i][j]))

        return edge_list

    def vertex_count(self):
        """Returns the number of vertices in the graph."""
        return self._vertices_count

    def edge_count(self):
        """Counts the number of edges in the graph."""
        #count = sum(sum(1 for val in row if val != 0) for row in self._adjMAT)

        # If undirected, each edge is counted twice, so divide by 2
        #return count if self._type == GraphType.DIRECTED else count // 2
        count = 0
        for i in range(self._vertices_count):
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != 0:
                    count += 1
        if self._type == GraphType.UNDIRECTED:
            count = count // 2

        return count

    def print_vertices(self):

        for i, v in enumerate(self.vertices):
            print(v, end=' ')
        print()

    # return the list of vertex index
    def get_neighbor_index_list(self, vertex_index):
        neighbor =[]
        for i in range(self._vertices_count):
            if self._adjMAT[vertex_index][i] != self.default_value:
                neighbor.append(i)
        return  neighbor

    # return the list of tuple which contain the index on vertex and it edges weight
    def get_neighbor_nodes(self, vertex_index):
        neighbor =[]
        for i in range(self._vertices_count):
            if self._adjMAT[vertex_index][i] != self.default_value:
                neighbor.append((i, self._adjMAT[vertex_index][i]))
        return  neighbor


    def breadth_first_search(self, start_vertex):
        """Performs BFS traversal from a given start vertex."""
        q = Queue()
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not found in graph.")

        start_vertex_index = self.vertices.index(start_vertex)
        visited = [False] * self._vertices_count

        # Mark start vertex as visited and enqueue it
        print(self.vertices[start_vertex_index], end=' ')
        visited[start_vertex_index] = True
        q.enqueue(start_vertex_index)

        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value and not visited[j]:
                    print(self.vertices[j], end=' ')
                    visited[j] = True
                    q.enqueue(j)
        print()

    def dfs_iterative(self, start_vertex):
        s = Stack()
        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not found in graph.")

        start_vertex_index = self.vertices.index(start_vertex)
        visited = [False] * self._vertices_count
        s.push(start_vertex_index)
        while not s.is_empty():
            i = s.pop()
            if not visited[i]:
                print(self.vertices[i], end=' ')
                visited[i] = True
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] > 0 and not visited[j]:
                    s.push(j)

        print()

    def dfs_recursive(self, start_vertex):

        if start_vertex not in self.vertices:
            raise ValueError("Start vertex not found in graph.")

        start_vertex_index = self.vertices.index(start_vertex)
        self.recursive_helper(start_vertex_index)
        print()

    def recursive_helper(self, index):
        if not self._visited[index]:
            print(self.vertices[index], end=' ')
            self._visited[index] = True

            for j in range(self._vertices_count):
                if self._adjMAT[index][j] > 0 and not self._visited[j]:
                    self.recursive_helper(j)


    def out_degree_vertex(self, v):
        """
        Returns the out-degree of a vertex `v` (i.e., number of edges starting from `v`).
        """
        if v not in self.vertices:
            raise ValueError("Start vertex not found in graph.")
        count = 0
        index = self.vertices.index(v)  # Get the index of the vertex
        for i in range(self._vertices_count):
            if self._adjMAT[index][i] != self.default_value:
                count += 1
        return count

    def in_degree_vertex(self, v):
        """
        Returns the in-degree of a vertex `v` (i.e., number of edges coming into `v`).
        """
        if v not in self.vertices:
            raise ValueError("Start vertex not found in graph.")
        count = 0
        index = self.vertices.index(v)  # Get the index of the vertex
        for i in range(self._vertices_count):
            if self._adjMAT[i][index] != self.default_value:
                count += 1
        return count

    def in_degrees(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {i: 0 for i,k in enumerate(self.vertices)}
        for i in range(self._vertices_count):  # Iterate through all vertices
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    degree[j] += 1  # Increment in-degree for destination vertex
        return degree  # Return the degree dictionary

    def out_degrees(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {i: 0 for i,k in enumerate(self.vertices)}
        for i in range(self._vertices_count):  # Iterate through all vertices
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    degree[i] += 1  # Increment out-degree for source vertex
        return degree  # Return the degree dictionary

    def degrees_print(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {"in": {k: 0 for k in self.vertices}, "out": {j: 0 for j in self.vertices}}
        for i in range(self._vertices_count):  # Iterate through all vertices
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    degree["out"][self.vertices[i]] += 1  # Increment out-degree for source vertex
                    degree["in"][self.vertices[j]] += 1  # Increment in-degree for destination vertex
        return degree  # Return the degree dictionary

    def display(self):
        """Displays the adjacency matrix in a formatted manner."""
        print("Adjacency Matrix:")
        header = "     |" + "|".join(f"{self.vertices[i]:^5}" for i in range(self._vertices_count)) + "|"
        print(header)
        print("-" * len(header))  # Top border

        # Print rows with corresponding vertex names
        for i in range(self._vertices_count):
            row = f"{self.vertices[i]:^5}|" + "|".join(
                f"{self._adjMAT[i][j]:^5}" for j in range(self._vertices_count)) + "|"
            print(row)
            print("-" * len(header))  # Row separator

        print("Vertices: ", self.vertex_count())
        print("Edges: ", self.edge_count())

    def plot_graph(self):
        """
        Plots the graph using NetworkX and Matplotlib.
        Displays (x, y) coordinates outside the vertex circle, near each vertex.
        Fixes arrow rendering issue for directed graphs.
        """
        # Choose directed or undirected graph type
        G = nx.DiGraph() if self._type == GraphType.DIRECTED else nx.Graph()

        # Add nodes
        for vertex in self.vertices:
            G.add_node(vertex)

        # Add edges and store weights (if weighted)
        edge_labels = {}
        for i in range(self._vertices_count):
            for j in range(self._vertices_count):
                if self._adjMAT[i][j] != self.default_value:
                    G.add_edge(self.vertices[i], self.vertices[j])
                    if self._weighted:
                        edge_labels[(self.vertices[i], self.vertices[j])] = self._adjMAT[i][j]

        # Assign node positions
        node_positions = {}
        assigned_positions = False

        for i, vertex in enumerate(self.vertices):
            if self._vertex_list[i]:  # If positions are available
                x, y = self._vertex_list[i].x, self._vertex_list[i].y
                node_positions[vertex] = (x, y)
                assigned_positions = True

        if not assigned_positions:  # If no predefined positions, generate them
            n = len(self.vertices)

            # Grid-based layout to avoid overlap
            rows = int(np.ceil(np.sqrt(n)))  # Number of rows in grid
            cols = int(np.ceil(n / rows))  # Number of columns

            for i, vertex in enumerate(self.vertices):
                x = (i % cols) * 2  # Grid spacing factor
                y = (i // cols) * 2
                node_positions[vertex] = (x, y)

            # Use Kamada-Kawai layout as a last resort
            node_positions = nx.kamada_kawai_layout(G, pos=node_positions)

        # Draw the graph
        plt.figure(figsize=(8, 8))
        nx.draw(
            G, pos=node_positions, with_labels=True, node_size=2000,
            node_color="lightblue", font_size=10, edge_color="black",
            arrows=True if self._type == GraphType.DIRECTED else False  # Fixes the arrow issue
        )

        # Draw edge labels if the graph is weighted
        if self._weighted:
            nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels, font_size=10)

        # Add (x, y) coordinates near the vertices (outside the circle)
        for vertex, (x, y) in node_positions.items():
            if vertex in self.vertices:
                vertex_index = self.vertices.index(vertex)
                if self._vertex_list[vertex_index]:  # Only display if coordinates are available
                    plt.text(x + 0.5, y + 0.5, f"({x}, {y})", fontsize=9, color="red")  # Slightly shifted from node

        plt.title("Graph Representation")
        plt.show()


# Sample execution
if __name__ == "__main__":
    g = Graph(5, GraphType.DIRECTED, weighted=True, default_val=0, vertices=['A', 'B', 'C', 'D', 'E'])

    g.insert_edge('A', 'B', 4)
    g.insert_edge('B', 'C', 2)
    g.insert_edge('B', 'D', 1)
    g.insert_edge('C', 'E', 8)
    g.insert_edge('E', 'D', 10)
    g.insert_edge('D', 'A', 5)

    # print(g.adjacency_matrix)
    g.display()

    print("\nEdges")
    g.print_edges()

    print("\nBFS:")
    g.breadth_first_search('B')

    print("\nDFS Iterative:")
    g.dfs_iterative('A')

    print("\nDFS Recursive:")
    g.dfs_recursive('A')

    print("\nDegree of Vertex:", end="")
    print(g.degrees_print())
    print(g.in_degrees())
    print(g.out_degrees())
    g.plot_graph()
