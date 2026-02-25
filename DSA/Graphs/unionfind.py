class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n
        self.max_size = 1

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        rx, ry = self.rank[px], self.rank[py]
        if rx < ry:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        self.max_size = max(self.max_size, self.size[rx])
        self.count -= 1
        return True

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_max_size(self) -> int:
        return self.max_size


class UnionFindString:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x: str) -> str:
        # initialize if not present
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            return x

        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

