# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if root is None:
            return None
        bfs_queue = [(root, 0)]
        last_right = root
        last_depth = -1
        while bfs_queue:
            node, depth = bfs_queue.pop(0)
            if node.left and node.right:
                bfs_queue.append((node.left, depth+1))
                bfs_queue.append((node.right, depth+1))
            if last_depth != depth:
                last_right.next = None
            else:
                last_right.next = node
            last_right = node
            last_depth = depth
        return root
