class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val) and
            is_valid_bst(root.right, root.val, high))


def insert_level_order(arr, i=0):
    if i < len(arr) and arr[i] is not None:
        node = TreeNode(arr[i])
        node.left = insert_level_order(arr, 2 * i + 1)
        node.right = insert_level_order(arr, 2 * i + 2)
        return node
    return None

inp = input("Enter tree nodes in list format (separated by commas) : ")
arr = eval(inp)  
root = insert_level_order(arr)
print("Is valid BST:", is_valid_bst(root))