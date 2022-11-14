# Visit the current node
# Traverse the current node's left subtree
# Travers the current node"S right subtree

from tree import tree

def preorder_walk(node):
    print(node.data)
    if node.left_child:
        preorder_walk(node.left_child)
    if node.right_child:
        preorder_walk(node.right_child)

preorder_walk(tree)
