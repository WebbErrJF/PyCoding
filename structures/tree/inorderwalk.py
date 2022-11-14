# Traverse the current node's left subtree
# Visit the current node
# Travers the current node"S right subtree
from tree import tree

def inorder_walk(node):
    if node.left_child:
        inorder_walk(node.left_child)
    print(node.data)
    if node.right_child:
        inorder_walk(node.right_child)
    
inorder_walk(tree)
