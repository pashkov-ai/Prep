from itertools import zip_longest


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leafSequenceIterator(node):
            if not node:
                return
            yield from leafSequenceIterator(node.left)
            if not node.left and not node.right:
                yield node.val
            yield from leafSequenceIterator(node.right)

        iter1 = leafSequenceIterator(root1)
        iter2 = leafSequenceIterator(root2)
        return all(a == b for a, b in zip_longest(iter1, iter2))