# todo: solve with DFS

class UnionFind:

    def __init__(self, s: str):
        self.source_string = s
        self.root = [i for i in range(len(s))]
        self.rank = [1] * len(s)

    def union(self, x: int, y: int) -> int: # O(a(V)) - time
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

    def find(self, x: int) -> int: # O(a(V)) - time
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def get_kv_components(self) -> dict[int, list]:
        kv = {} # O(V) - space
        for i in range(len(self.root)): # O(V) -time
            iroot = self.find(i)
            kv.setdefault(iroot, []).append(self.source_string[i]) # todo: optimize using bisect
        for k, v in kv.items(): # O(V log V) - time
            v.sort(reverse=True)
        return kv

    def get_smallest_string(self) -> str:
        # O(a(V) * V + V log V) - time, O(V) - space
        smallest_str_builder = [] # O(V) - space
        kv = self.get_kv_components() # O(V log V) - time, O(V) - space
        for i in range(len(self.root)): # O(a(V) * V) - time
            ch = kv[self.find(i)].pop() # O(a(V))
            smallest_str_builder.append(ch)
        return ''.join(smallest_str_builder) # O(V) - time, space


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        # init unionfind on pairs
        # V = len(s), E = len(pairs)
        # O( a(V) * (E + V)  + V logV) - time, O(V) - space
        uf = UnionFind(s) # O(V) - space,
        for (i, j) in pairs: # O(a(V) * E)- time
            uf.union(i, j)
        # split chars by components, sort them desc in each group (kv value)
        # iterate over uf root array and put lowest char in kv dict string. poping last elem
        return uf.get_smallest_string() # O(a(V) * V + V log V) - time, O(V) - space