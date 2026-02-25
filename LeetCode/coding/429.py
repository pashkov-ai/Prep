from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []



class Solution:
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        serialization = []
        if root is None:
            return serialization

        bfs_queue = deque()
        bfs_queue.append((root, 0))
        while bfs_queue:
            node, depth = bfs_queue.popleft()
            if len(serialization) <= depth:
                serialization.append([])
            serialization[depth].append(node.val)
            if node.children is None:
                continue
            for child in node.children:
                bfs_queue.append((child, depth + 1))
        return serialization
