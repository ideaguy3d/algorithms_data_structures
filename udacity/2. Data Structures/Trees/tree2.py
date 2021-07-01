
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.__root = None

    def traverse_preorder(self):
        def preorder(node: Node):
            if not node: return
            print(node.value)
            preorder(node.left)
            preorder(node.right)
        preorder(self.__root)

    def traverse_preorder_iter(self):
        node_stack = [self.__root]
        while len(node_stack):
            node = node_stack.pop()
            print(node.value)
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
            


br = 1


# end of file