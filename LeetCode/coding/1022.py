# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Morris traversal w/ modifications
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        bin_sum = 0
        curr_num = 0

        cur = root
        while cur:
            if cur.left is None:  # no left tree
                # do preorder
                curr_num = (curr_num << 1) | cur.val
                if cur.right is None:  # is leaf, not counting backtracking leafs
                    bin_sum += curr_num
                cur = cur.right  # go to right subtree
            else:  # left subtree
                pred = cur.left
                steps = 1
                while pred.right and pred.right != cur:  # get rightmost
                    pred = pred.right
                    steps += 1

                if pred.right is None:  # haven't explored yet
                    # do preorder
                    curr_num = (curr_num << 1) | cur.val
                    pred.right = cur  # set-up the backtrack link
                    cur = cur.left  # explore left subtree
                else:  # have been there, backtrack
                    if pred.left is None:  # a leaf w/ backtrack right link
                        bin_sum += curr_num
                    pred.right = None  # restore tree
                    cur = cur.right  # explore right subtree now / backtrack
                    curr_num >>= steps
        return bin_sum