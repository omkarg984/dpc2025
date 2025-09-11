class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_list):
    """Build a binary tree from a list using level-order representation."""
    if not level_list:
        return None
    nodes = [None if v is None else TreeNode(v) for v in level_list]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def is_mirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val) and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

def is_symmetric(root):
    return is_mirror(root.left, root.right) if root else True

# ---- Main Program ----
# Example input: 1 2 2 3 4 4 3
user_input = input("Enter tree nodes in level order (use None for missing nodes): ")
# Convert input into Python list
values = []
for x in user_input.split():
    values.append(None if x.lower() == "none" else int(x))

root = build_tree(values)
print("Is the tree symmetric?", is_symmetric(root))