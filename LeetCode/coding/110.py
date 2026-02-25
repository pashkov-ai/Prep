# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(node: TreeNode | None, depth: int) -> tuple[bool, int]:
            if node is None:
                return True, depth - 1

            is_left_balanced, left_max_depth = dfs(node.left, depth + 1)
            is_right_balanced, right_max_depth = dfs(node.right, depth + 1)
            if is_left_balanced == is_right_balanced == True and abs(left_max_depth - right_max_depth) < 2:
                return True, max(left_max_depth, right_max_depth)
            return False, max(left_max_depth, right_max_depth)

        is_balanced, max_depth = dfs(root, 1)
        return is_balanced