# This class is for AStar
class Vertex:
    def __init__(self, x=None, y= None, name=None, index_position= None):
        # Below properties are for AStar Search algorithm
        self.name = name
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.g = float('inf')  # Cost from start node
        self.f = float('inf')  # Total cost (g + heuristic)
        self.parent = None
        self.index_position = index_position

    def __lt__(self, other):
        return self.f < other.f  # Needed for priority queue

    def __repr__(self):
        return self.name