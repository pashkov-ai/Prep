class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        source, dest = 0, n - 1
        valid_paths = []
        # no seen cuz its guaranteed to be DAG

        def dfs(node: int, path: list[int]) -> None:
            if node == dest:
                valid_paths.append(path.copy())
                return

            for adj_node in graph[node]:
                path.append(adj_node)
                dfs(adj_node, path)
                path.pop()

        dfs(source, [source])
        return valid_paths