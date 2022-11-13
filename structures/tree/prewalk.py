# object to store information about node
class BTS:
    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None

    def insert(self,data): #adding new node to the tree
        if data>self.data: #condition to make keep tree as BST
            if self.right_child is None:
                self.right_child=BTS(data)
            else:
                self.right_child.insert(data)
        else:
            if self.left_child is None:
                self.left_child=BTS(data)
            else:
                self.left_child.insert(data)

    #def remove()

    #def search()

tree=BTS(25)
tree.insert(50)
tree.insert(10)
tree.insert(85)
tree.insert(36)
tree.insert(3)
tree.insert(6)
tree.insert(12)
tree.insert(18)
tree.insert(20)

print(tree.right_child.left_child.right_child.left_child.data)