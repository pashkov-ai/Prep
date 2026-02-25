
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        # O(V + E) - time, O(V) - space
        if node is None:
            return None

        seen = {}

        def dfs(current_node):
            current_node_copy = Node(current_node.val)
            seen[current_node.val] = current_node_copy

            for adj_node in current_node.neighbors:
                adj_node_copy = seen[adj_node.val] if adj_node.val in seen else dfs(adj_node)
                current_node_copy.neighbors.append(adj_node_copy)
            return current_node_copy

        return dfs(node)
