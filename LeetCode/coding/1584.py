class UnionFind:

    def __init__(self, size: int):
        # O(V) - time, space
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def union(self, x: int, y: int) -> bool:
        # O(a(V)) - time
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        rx, ry = self.rank[px], self.rank[py]
        if rx < ry:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True

    def find(self, x: int) -> int:
        # O(a(V)) - time
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def is_connected(self, x: int, y: int) -> bool:
        # O(a(V)) - time
        return self.find(x) == self.find(y)


class SolutionKruskal:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # O(V^2 * (log V + a(V))) - time, O(V^2) - space

        def manhattan_distance(p0: list[int], p1: list[int]) -> int:
            # O(1) - time, space
            x0, y0 = p0
            x1, y1 = p1
            return abs(x0 - x1) + abs(y0 - y1)

        n = len(points)
        # calculate pair wise distances
        # O(V^2) - time, space
        distances = [(i, j, manhattan_distance(points[i], points[j])) for i in range(n) for j in range(i + 1, n)]

        # sort distances asc
        # O(V^2 log V^2) == O(V^2 log V) - time, O(V logV) - space (TimSort)
        distances.sort(key=lambda x: x[2])

        # kruskal:
        # * sort edges asc
        # * for each edge: add edge if not cycle (Union-Find) until V-1 edges added
        uf = UnionFind(n)  # O(V) - time, space
        min_cost = 0
        edges_added = 0
        for (i, j, dist) in distances:  # O(V^2)
            if uf.is_connected(i, j):  # O(a(V))
                continue
            uf.union(i, j)  # O(a(V))
            min_cost += dist
            edges_added += 1
            if edges_added == n - 1:
                break
        return min_cost

import math
class SolutionPrim:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # O(V^2) - time, O(V) - space

        def manhattan_distance(p0: list[int], p1: list[int]) -> int:
            # O(1) - time, space
            x0, y0 = p0
            x1, y1 = p1
            return abs(x0 - x1) + abs(y0 - y1)

        n = len(points)
        min_cost = 0

        min_dist_to_node = {i: math.inf for i in range(n)}  # O(V) - time, space
        min_dist_to_node[0] = 0
        for _ in range(n): # O(V) - time
            # pick node with the lowest distance
            curr_node = min(min_dist_to_node, key=lambda i: min_dist_to_node[i]) # O(V) - time
            min_cost += min_dist_to_node[curr_node]
            min_dist_to_node.pop(curr_node)

            # update dists from newly added node to the component
            for k in min_dist_to_node.keys(): # O(V) - time
                dist = manhattan_distance(points[curr_node], points[k]) # O(1) - time
                min_dist_to_node[k] = min(min_dist_to_node[k], dist)
        return min_cost

