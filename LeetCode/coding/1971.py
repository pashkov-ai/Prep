class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # V == n, E - len(edges)
        # O(V + E) - time, O(V + E) - space
        # create connectivity
        adjacency = {} # O(E) - space
        for (i, j) in edges: # O(E) - time
            adjacency.setdefault(i, []).append(j)
            adjacency.setdefault(j, []).append(i)
        # stack DFS
        visited = [False] * n # O(V) - time/space
        visited[source] = True
        stack = [source] # O(V) - space
        while stack: # O(V + E) - time
            inode = stack.pop()
            if inode == destination:
                return True
            for i in adjacency[inode]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        return False