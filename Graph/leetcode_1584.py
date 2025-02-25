from typing import List


def minCostConnectPoints(points: List[List[int]]) -> int:

    def find(parent, vertex):
        if parent[vertex] != vertex:
            return find(parent, parent[vertex])
        return vertex

    def union(parent, x, y):
        x_Parent = find(parent, x)
        y_Parent = find(parent, y)
        parent[y_Parent] = x_Parent

    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((cost,i,j))

    edges.sort()

    parent = [i for i in range(n)]
    mst_cost = 0
    number_edge = 0
    for cost,u,v in edges:
        x_set = find(parent, u)
        y_set = find(parent, v)
        if x_set==y_set:
            continue
        else:
            number_edge += 1
            union(parent, x_set, y_set)
            mst_cost += cost

            if number_edge == n-1:
                break

    return mst_cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

print(minCostConnectPoints(points))

