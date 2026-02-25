class UnionFind:

    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> None:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        rankX, rankY = self.rank[rootX], self.rank[rootY]
        if rankX < rankY:
            self.root[rootX] = rootY
        elif rankX > rankY:
            self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def get_union_count(self) -> int:
        return sum(self.root[i] == i for i in range(len(self.root)))


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union_find.union(i, j)
        return union_find.get_union_count()