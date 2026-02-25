class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(node: TreeNode | None) -> None:
    if node is None:
        return
    print(node.val)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order_traversal(node: TreeNode | None) -> None:
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.val)
    in_order_traversal(node.right)

def post_order_traversal(node: TreeNode | None) -> None:
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.val)

def pre_order_traversal_stack(root: TreeNode | None) -> None:
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    pass

def in_order_traversal_stack(root: TreeNode | None) -> list[int]:
    array = list()
    curr = root
    stack = list()
    while curr or stack:
        # go as left as possible
        while curr:
            stack.append(curr)
            curr = curr.left
        # process node
        curr = stack.pop()
        array.append(curr.val)
        # then go right
        curr = curr.right
    return array

def post_order_traversal_2stack(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    s1 = [root]
    s2 = []
    res = []

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        res.append(s2.pop().val)

    return res


def post_order_traversal_stack(root: TreeNode | None) -> list[int]:
    res = []
    stack = []
    last_visited = None
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                last_visited = stack.pop()

    return res


def morris(root: TreeNode | None) -> list[int]:
    res = []
    cur = root
    while cur:
        if cur.left is None: # no left subtree
            # DO PREORDER / INORDER
            # IS_LEAF
            cur = cur.right # go right
        else: # left subtree exists
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right # get rightmost node in left subtree
            if pred.right is None: # haven't visited left subtree yet
                # DO PREORDER
                pred.right = cur # set-up backtrack link
                cur = cur.left # explore left subtree
            else: # backtracking
                # IS_LEAF - check for leaf here, cuz we modified pred.right from None
                pred.right = None # restore tree
                # DO IN_ORDER
                cur = cur.right # go to right subtree, as left has been explored
    return res

# in-place traversal
def morris_preorder(root: TreeNode | None) -> list[int]:
    res = []
    cur = root

    while cur:
        if cur.left is None:
            res.append(cur.val)
            cur = cur.right
        else:
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right

            if pred.right is None:
                res.append(cur.val)   # visit BEFORE threading
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                cur = cur.right

    return res


# in-place traversal
def morris_inorder(root: TreeNode | None) -> list[int]:
    res = []
    cur = root

    while cur:
        if cur.left is None:
            res.append(cur.val)
            cur = cur.right
        else:
            # find predecessor (rightmost of left subtree)
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right

            if pred.right is None:
                # create thread
                pred.right = cur
                cur = cur.left
            else:
                # thread exists -> remove it
                pred.right = None
                res.append(cur.val)
                cur = cur.right

    return res


def morris_postorder(root: TreeNode | None) -> list[int]:
    res = []
    dummy = TreeNode(0)
    dummy.left = root
    cur = dummy

    def reverse_path(start: TreeNode, end: TreeNode):
        prev = None
        cur = start
        while cur != end:
            nxt = cur.right
            cur.right = prev
            prev = cur
            cur = nxt
        cur.right = prev

    def collect_reverse(start: TreeNode, end: TreeNode):
        reverse_path(start, end)
        node = end
        while True:
            res.append(node.val)
            if node == start:
                break
            node = node.right
        reverse_path(end, start)

    while cur:
        if cur.left is None:
            cur = cur.right
        else:
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right

            if pred.right is None:
                # create thread
                pred.right = cur
                cur = cur.left
            else:
                # thread exists: process left subtree
                collect_reverse(cur.left, pred)
                pred.right = None
                cur = cur.right

    return res

