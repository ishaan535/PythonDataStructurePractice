import sys

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp

from Graph.AdjacencyNode import AdjacencyEdgeNode
from Graph.Vertex import Vertex
from Graph.GraphType import GraphType
from Queues.QueueUsingLL import Queue

sys.path.append('.')

class Graph:

    def __init__(self, vertices_count, graph_type=GraphType.DIRECTED, weighted=False, vertices=None):
        if vertices is None:
            self.vertices = [i for i in range(vertices_count)]  # Default vertices as range indices
        else:
            if vertices_count != len(vertices):
                raise ValueError("Vertex count don't match with list of vertex")
            self.vertices = vertices  # Custom vertex labels

        self._vertices_count = vertices_count  # Number of vertices
        self._type = graph_type  # Graph type (directed/undirected)
        self._weighted = weighted  # Flag indicating if the graph is weighted
        self._adj_list = [None] * vertices_count  # Adjacency list initialized with None
        self._visited = [False] * self._vertices_count  # Visited list for graph traversal
        self._vertex_list = [None] * vertices_count # Storing the node list so that can be used in AStar Search

    @property
    def adjacency_list(self):
        return self._adj_list

    @property
    def vertex_list(self):
        return self._vertex_list

    def insert_edge(self, vertex_u, vertex_v, weight=1):
        if vertex_u not in self.vertices or vertex_v not in self.vertices:
            raise ValueError("One or both vertices are not in the graph.")

        u = self.vertices.index(vertex_u)  # Get index of source vertex
        v = self.vertices.index(vertex_v)  # Get index of destination vertex

        # Insert at the beginning of adjacency list for vertex u
        new_node = AdjacencyEdgeNode(v, weight)
        new_node.next = self._adj_list[u]
        self._adj_list[u] = new_node

        # If the graph is undirected, insert the reverse edge
        if self._type == GraphType.UNDIRECTED:
            new_node = AdjacencyEdgeNode(u, weight)
            new_node.next = self._adj_list[v]
            self._adj_list[v] = new_node

    def add_vertex(self, vertex, x,y):
        if vertex not in self.vertices :
            raise ValueError("One or both vertices are not in the graph.")
        vertex_index = self.vertices.index(vertex)
        self._vertex_list[vertex_index] = Vertex(x, y, vertex, vertex_index)

    def remove_edge(self, vertex_u, vertex_v):
        if vertex_u not in self.vertices or vertex_v not in self.vertices:
            raise ValueError("One or both vertices are not in the graph.")

        u = self.vertices.index(vertex_u)
        v = self.vertices.index(vertex_v)

        # Helper function to remove node from adjacency list
        def remove_node(head, target):
            prev, curr = None, head
            while curr:
                if curr.vertex == target:
                    if prev:
                        prev.next = curr.next  # Remove current node
                    else:
                        head = curr.next  # Update head if first node is removed
                    return head
                prev, curr = curr, curr.next
            return head  # Return modified head

        self._adj_list[u] = remove_node(self._adj_list[u], v)
        if self._type == GraphType.UNDIRECTED:
            self._adj_list[v] = remove_node(self._adj_list[v], u)

    def exist_edge(self, u, v):
        temp = self._adj_list[u]
        while temp:
            if temp.vertex == v:
                return True
            temp = temp.next
        return False

    def get_edge_weight(self,u,v):
        temp = self._adj_list[u]
        while temp:
            if temp.vertex == v:
                return temp.weight
            temp = temp.next
        return  None

    def print_edges(self):
        """Prints all edges in the graph."""
        for i in range(self._vertices_count):
            temp = self._adj_list[i]
            while temp:
                if self._weighted:
                    print(f'{self.vertices[i]} -- {self.vertices[temp.vertex]} = {temp.weight}')
                else:
                    print(f'{self.vertices[i]} -- {self.vertices[temp.vertex]}')
                temp = temp.next

    def get_edges(self):
        edge_list = []
        for i in range(self._vertices_count):
            temp = self._adj_list[i]
            while temp:
                edge_list.append((i, temp.vertex, temp.weight))
                temp = temp.next

        return edge_list

    def vertex_count(self):
        """Returns the total number of vertices in the graph."""
        return self._vertices_count

    def edge_count(self):
        """Returns the total number of edges in the graph."""
        count = 0
        for i in range(self._vertices_count):
            temp = self._adj_list[i]
            while temp:
                count += 1
                temp = temp.next
        if self._type == GraphType.UNDIRECTED:
            count = count // 2
        return  count
        # return count if self._type == GraphType.DIRECTED else count // 2

    def print_vertices(self):
        """Prints all vertices in the graph."""
        print("Vertices:", ' '.join(map(str, self.vertices)))

    def get_neighbor_index_list(self, vertex_index):
        neighbor =[]
        temp = self._adj_list[vertex_index]  # Get adjacency list of vertex `i`
        while temp:  # Traverse adjacency list
            neighbor.append(temp.vertex)
            temp = temp.next  # Move to the next adjacent vertex
        return  neighbor

    def get_neighbor_nodes(self, vertex_index):
        neighbor =[]
        temp = self._adj_list[vertex_index]  # Get adjacency list of vertex `i`
        while temp:  # Traverse adjacency list
            neighbor.append((temp.vertex, temp.weight))
            temp = temp.next  # Move to the next adjacent vertex
        return  neighbor

    def breadth_first_search(self, start_vertex):
        """
        Performs BFS traversal starting from `start_vertex`.
        Prints vertices in the order they are visited.
        """
        q = Queue()  # Queue to store vertices to be processed
        visited = [False] * self._vertices_count  # Track visited vertices
        start_index = self.vertices.index(start_vertex)  # Get index of start vertex
        print(self.vertices[start_index], end=' ')  # Print starting vertex
        visited[start_index] = True  # Mark it as visited
        q.enqueue(start_index)  # Enqueue start vertex

        while q:  # Process the queue until empty
            i = q.dequeue() # Dequeue vertex `i`
            temp = self._adj_list[i]  # Get adjacency list of `i`
            while temp:  # Traverse adjacency list
                if not visited[temp.vertex]:  # If the vertex is unvisited
                    print(self.vertices[temp.vertex], end=' ')  # Print vertex
                    visited[temp.vertex] = True  # Mark it as visited
                    q.enqueue(temp.vertex)  # Enqueue vertex
                temp = temp.next  # Move to next adjacent vertex
        print()  # New line after traversal

    def dfs_iterative(self, start_vertex):
        """
        Performs iterative DFS traversal starting from `start_vertex`.
        Prints vertices in the order they are visited.
        """
        s = []  # Stack for DFS
        start_index = self.vertices.index(start_vertex)  # Get index of start vertex
        visited = [False] * self._vertices_count  # Track visited vertices
        s.append(start_index)  # Push start vertex to stack

        while s:  # Process stack until empty
            i = s.pop()  # Pop vertex `i` from stack
            if not visited[i]:  # If not visited
                print(self.vertices[i], end=' ')  # Print vertex
                visited[i] = True  # Mark as visited
            temp = self._adj_list[i]  # Get adjacency list of `i`
            while temp:  # Traverse adjacency list
                if not visited[temp.vertex]:  # If adjacent vertex is unvisited
                    s.append(temp.vertex)  # Push vertex to stack
                temp = temp.next  # Move to next adjacent vertex
        print()  # New line after traversal

    def dfs_recursive(self, start_vertex):
        """
        Performs recursive DFS traversal starting from `start_vertex`.
        Prints vertices in the order they are visited.
        """
        start_index = self.vertices.index(start_vertex)  # Get index of start vertex
        self._visited = [False] * self._vertices_count  # Reset visited array before traversal
        self._dfs_recur_helper(start_index)  # Start recursive DFS traversal
        print()  # New line after traversal

    def _dfs_recur_helper(self, vertex_index):
        """
        Helper function for DFS recursive traversal.
        """
        if not self._visited[vertex_index]:  # If vertex has not been visited
            print(self.vertices[vertex_index], end=' ')  # Print current vertex
            self._visited[vertex_index] = True  # Mark vertex as visited

            temp = self._adj_list[vertex_index]  # Get adjacency list of the vertex
            while temp:  # Traverse adjacency list
                if not self._visited[temp.vertex]:  # If adjacent vertex is unvisited
                    self._dfs_recur_helper(temp.vertex)  # Recur for adjacent vertex
                temp = temp.next  # Move to next adjacent vertex

    def out_degree_vertex(self, v):
        """
        Returns the out-degree of a vertex `v` (i.e., number of edges starting from `v`).
        """
        count = 0
        u = self.vertices.index(v)  # Get the index of the vertex
        temp = self._adj_list[u]  # Retrieve the adjacency list for this vertex
        while temp:  # Traverse the adjacency list
            count += 1  # Increment count for each outgoing edge
            temp = temp.next  # Move to the next adjacent vertex
        return count  # Return the total count of outgoing edges

    def in_degree_vertex(self, v):
        """
        Returns the in-degree of a vertex `v` (i.e., number of edges coming into `v`).
        """
        count = 0
        v_index = self.vertices.index(v)  # Get the index of the vertex
        for i in range(self._vertices_count):  # Iterate over all vertices
            temp = self._adj_list[i]  # Get the adjacency list of vertex `i`
            while temp:  # Traverse its adjacency list
                if temp.vertex == v_index:  # If `v_index` is found, it means an incoming edge
                    count += 1  # Increment count
                temp = temp.next  # Move to the next adjacent vertex
        return count  # Return the total count of incoming edges

    def degrees_print(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {"in": {k: 0 for k in self.vertices}, "out": {j: 0 for j in self.vertices}}
        for i in range(self._vertices_count):  # Iterate through all vertices
            temp = self._adj_list[i]  # Get adjacency list of vertex `i`
            while temp:  # Traverse adjacency list
                degree["out"][self.vertices[i]] += 1  # Increment out-degree for source vertex
                degree["in"][self.vertices[temp.vertex]] += 1  # Increment in-degree for destination vertex
                temp = temp.next  # Move to the next adjacent vertex
        return degree  # Return the degree dictionary

    def in_degrees(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {i: 0 for i,k in enumerate(self.vertices)}
        for i in range(self._vertices_count):  # Iterate through all vertices
            temp = self._adj_list[i]  # Get adjacency list of vertex `i`
            while temp:  # Traverse adjacency list
                degree[temp.vertex] += 1  # Increment in-degree for destination vertex
                temp = temp.next  # Move to the next adjacent vertex
        return degree  # Return the degree dictionary

    def out_degrees(self):
        """
        Returns a dictionary containing in-degree and out-degree for all vertices.
        """
        degree = {i: 0 for i,k in enumerate(self.vertices)}
        for i in range(self._vertices_count):  # Iterate through all vertices
            temp = self._adj_list[i]  # Get adjacency list of vertex `i`
            while temp:  # Traverse adjacency list
                degree[i] += 1  # Increment out-degree for source vertex
                temp = temp.next  # Move to the next adjacent vertex
        return degree  # Return the degree dictionary

    def display(self):
        """Displays the adjacency list of the graph."""
        print("Adjacency List:")
        for i in range(self._vertices_count):
            print(f'{self.vertices[i]}:', end='')
            temp = self._adj_list[i]
            while temp:
                if self._weighted:
                    print(f' -> {self.vertices[temp.vertex]}({temp.weight})', end='')
                else:
                    print(f' -> {self.vertices[temp.vertex]}', end='')
                temp = temp.next
            print()
        print("Total Vertices:", self.vertex_count())
        print("Total Edges:", self.edge_count())

    def plot_graph(self):
        """
        Plots the graph using NetworkX and Matplotlib.
        Displays (x, y) coordinates near each vertex.
        Uses a structured layout to minimize edge crossings.
        """
        # Choose directed or undirected graph type
        is_directed = self._type == GraphType.DIRECTED
        G = nx.DiGraph() if is_directed else nx.Graph()

        # Add nodes
        for vertex in self.vertices:
            G.add_node(vertex)

        # Add edges and store weights (if weighted)
        edge_labels = {}
        for i, vertex in enumerate(self.vertices):
            temp = self._adj_list[i]  # Access adjacency list
            while temp:
                G.add_edge(vertex, self.vertices[temp.vertex])  # Add edge
                if self._weighted:
                    edge_labels[(vertex, self.vertices[temp.vertex])] = temp.weight  # Store edge weight
                temp = temp.next  # Move to the next adjacent node

        # Assign node positions: Use given (x, y) or generate them
        node_positions = {}
        assigned_positions = False

        for i, vertex in enumerate(self.vertices):
            if self._vertex_list[i]:  # If (x, y) positions are available
                x, y = self._vertex_list[i].x, self._vertex_list[i].y
                node_positions[vertex] = (x, y)
                assigned_positions = True

        if not assigned_positions:  # If no predefined positions, generate them
            n = len(self.vertices)

            # Grid-based layout to reduce overlap
            rows = int(np.ceil(np.sqrt(n)))  # Number of rows in grid
            cols = int(np.ceil(n / rows))  # Number of columns

            for i, vertex in enumerate(self.vertices):
                x = (i % cols) * 2  # Grid spacing factor
                y = (i // cols) * 2
                node_positions[vertex] = (x, y)

            # Use Kamada-Kawai layout as a fallback for better edge clarity
            node_positions = nx.kamada_kawai_layout(G, pos=node_positions)

        # Draw the graph
        plt.figure(figsize=(8, 8))
        nx.draw(G, pos=node_positions, with_labels=True, node_size=2000,
                node_color="lightblue", font_size=10, edge_color="black",
                arrows=is_directed)  # Use arrows=True instead of arrowstyle

        # Draw edge labels for weighted graphs
        if self._weighted:
            nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels, font_size=10)

        # Display (x, y) coordinates near each vertex
        for vertex, (x, y) in node_positions.items():
            vertex_index = self.vertices.index(vertex)
            if self._vertex_list[vertex_index]:  # Only display if coordinates exist
                plt.text(x + 0.5, y + 0.5, f"({x:.1f}, {y:.1f})", fontsize=10, color="red")

        plt.title("Graph Representation")
        plt.show()

if __name__ == "__main__":
    g = Graph(5, GraphType.UNDIRECTED, weighted=True, vertices=['A', 'B', 'C', 'D', 'E'])

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
    g.breadth_first_search('A')

    print("\nDFS Iterative:")
    g.dfs_iterative('A')

    print("\nDFS Recursive:")
    g.dfs_recursive('A')

    print("\nDegree of Vertex:", end="")
    print(g.degrees_print())
    print(g.in_degrees())
    print(g.out_degrees())
    g.plot_graph()
