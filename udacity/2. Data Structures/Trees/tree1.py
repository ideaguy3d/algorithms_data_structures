
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_right_child(self, value):
        self.right = value

    def set_left_child(self, value):
        self.left = value

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_right_child(self):
        return not not self.right

    def has_left_child(self):
        return not not self.left

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

n1 = Node('apple')
n2 = Node('blue berry')
n3 = Node('rasberry')

print(f'n1 has left child? {n1.has_left_child()}')
print(f'n2 has right child? {n1.has_right_child()}')

print('\nadding left & right children\n')
n1.set_left_child(n2)
n1.set_right_child(n3)

print(f'n1 has left child? {n1.has_left_child()}')
print(f'n2 has right child? {n1.has_right_child()}')

tree = Tree('apple')
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


debug = 1

# end of file