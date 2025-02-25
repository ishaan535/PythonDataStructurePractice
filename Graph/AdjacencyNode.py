
class AdjacencyEdgeNode:
    """
    Class representing an adjacency list node.
    Each node contains:
        - vertex index (destination vertex)
        - weight (if the graph is weighted)
        - next pointer (link to the next node in the adjacency list)
    """
    def __init__(self, vertex_index: int, weight: int = None):
        self.vertex = vertex_index  # Destination vertex index
        self.weight = weight  # Weight of the edge (if applicable)
        self.next = None  # Pointer to the next adjacent vertex