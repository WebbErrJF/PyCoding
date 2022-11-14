# Traverse the current node's left subtree
# Travers the current node"S right subtree
# Visit the current node

from tree import tree

def postorder_walk(node):
    if node.left_child:
        postorder_walk(node.left_child)
    if node.right_child:
        postorder_walk(node.right_child)
    print(node.data)

postorder_walk(tree)