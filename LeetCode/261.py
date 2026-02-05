class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def union(self, x: int, y: int) -> int:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return rootX
        rankX, rankY = self.rank[rootX], self.rank[rootY]
        if rankX < rankY:
            self.root[rootX] = rootY
        elif rankX > rankY:
            self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return self.root[rootX]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_component_count(self) -> int:
        return sum(self.root[i] == i for i in range(len(self.root)))


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        uf = UnionFind(n)
        for (i, j) in edges:
            if uf.is_connected(i, j):
                return False
            uf.union(i, j)
        return uf.get_component_count() == 1
