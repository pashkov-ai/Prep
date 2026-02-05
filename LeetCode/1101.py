class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.n_components = n

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
        self.n_components -= 1
        return self.root[rootX]

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_components_count(self) -> int:
        return self.n_components


class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort(key = lambda x: x[0])
        for (ts, x, y) in logs:
            uf.union(x, y)
            if uf.get_components_count() == 1:
                return ts
        return -1