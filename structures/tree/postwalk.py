# Traverse the current node's left subtree
# Travers the current node"S right subtree
# Visit the current node

class BTS:
    def __init__(self, data): #creating the root
        self.left_child = None
        self.data = data
        self.right_child = None

    def insert(self,data): #adding new node to the tree
        if data>self.data: #condition to keep tree as BST, any value that is greater than value of the root goes to the right 
            if not self.right_child:
                self.right_child=BTS(data)
            else: #if node allready exists call recursion
                self.right_child.insert(data)
        else:   #condition to keep tree as BST, any value that is greater than value of the root goes to the right 
            if not self.left_child:
                self.left_child=BTS(data)
            else: #if node allready exists call recursion
                self.left_child.insert(data)

    def postorder_walk(self):
        if self.left_child:
            self.left_child.postorder_walk()
        if self.right_child:
            self.right_child.postorder_walk()
        print(self.data)

tree=BTS(25)
tree.insert(20)
tree.insert(22)
tree.insert(19)
tree.insert(21)
tree.insert(23)
tree.insert(27)
tree.insert(26)
tree.insert(28)
tree.postorder_walk()