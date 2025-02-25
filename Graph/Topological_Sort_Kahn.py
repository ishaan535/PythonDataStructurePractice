from collections import deque
from typing import List



def topological_sort(num_vertex: int , edges: List[List[int]])-> List[int]:
    graph = build_graph(num_vertex,edges)
    inDegree = {x: 0 for x in range(num_vertex)}
    for vertex, neighbours in graph.items():
        for y in neighbours:
            inDegree[y] += 1

    source = deque()
    for vertex, value in inDegree.items():
        if value == 0:
            source.append(vertex)

    order = []
    step = 1

    while len(source) > 0:
        print("Step Number: ", step)
        print("In Degree: ", inDegree)
        print("Source: " , source)
        print("Order: ", order)
        print("")
        step += 1
        current_vertex = source.popleft()
        order.append(current_vertex)
        for y in graph[current_vertex]:
            inDegree[y] -= 1
            if inDegree[y] == 0:
                source.append(y)

    if len(order) == num_vertex:
        return order

    return []

def build_graph(num_vertex: int, edges: List[List[int]])-> dict:
    graph = {x: [] for x in range(num_vertex)}
    for edge in edges:
        a, b = edge
        graph[a].append(b)
    return graph


if __name__  ==  "__main__":
    num_vertex = 8
    edges = [[7,5],[7,6],[5,4],[6,4],[5,2],[6,3],[2,1],[3,1],[1,0]]
    result = topological_sort(num_vertex, edges)
    print("Topological Sort: ", result)

    #print(build_graph(num_vertex, edges))