class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Builds a binary tree from a list (level order)."""
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: 
                node.left = kids.pop()
            if kids: 
                node.right = kids.pop()
    return root

def lowestCommonAncestor(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right


# ----------------- User Input -----------------
values = input("Enter tree nodes in level-order (use 'null' for None, separated by spaces):\n")
values = [None if v.lower() == "null" else int(v) for v in values.split()]

p = int(input("Enter value of node p: "))
q = int(input("Enter value of node q: "))

# Build tree
root = build_tree(values)

# Find LCA
lca = lowestCommonAncestor(root, p, q)
print(f"Lowest Common Ancestor of {p} and {q}: {lca.val if lca else None}")