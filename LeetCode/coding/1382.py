# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:

        # create sorted array using in-order traversal
        def in_order_traversal(root: TreeNode | None) -> list[int]:
            sorted_array = list()
            curr = root
            stack = list()
            while curr or stack:
                # go as left as possible
                while curr:
                    stack.append(curr)
                    curr = curr.left
                # process node
                curr = stack.pop()
                sorted_array.append(curr.val)
                # then go right
                curr = curr.right
            return sorted_array

        # create bst from the array
        def make_tree(sorted_array: list[int]) -> TreeNode | None:
            n = len(sorted_array)
            if n == 0:
                return None

            root = TreeNode()
            stack = [(0, n - 1, root)]
            while stack:
                l, r, node = stack.pop()
                mid = (r - l) // 2 + l
                node.val = sorted_array[mid]
                if l < mid:
                    node.left = TreeNode()
                    stack.append((l, mid - 1, node.left))
                if mid < r:
                    node.right = TreeNode()
                    stack.append((mid + 1, r, node.right))
            return root

        sorted_array = in_order_traversal(root)
        root_balanced = make_tree(sorted_array)
        return root_balanced
