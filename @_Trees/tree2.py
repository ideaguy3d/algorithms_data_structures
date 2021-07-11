import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def output(value):
    if not BinaryTree.testing:
        print(value)


class BinaryTree:
    testing = True

    def __init__(self, c_root_node):
        self.__root = c_root_node

    def preorder_traverse(self):
        _list = []

        def preorder(node: Node):
            if not node: return
            _list.append(node.value)
            output(node.value)
            preorder(node.left)
            preorder(node.right)

        preorder(self.__root)
        return _list

    def preorder_traverse_iter(self):
        _list = []
        node_stack = [self.__root]
        while len(node_stack):
            node = node_stack.pop()
            _list.append(node.value)
            output(node.value)
            if node.right:
                node_stack.append(node.right)
            if node.left:
                node_stack.append(node.left)
        return _list

    def inorder_traverse(self):
        def inorder(node: Node):
            if not node: return
            inorder(node.left)
            print(node.value)
            inorder(node.right)

        inorder(self.__root)

    def inorder_traverse_iter(self):
        """
        result_1 = [10, 41, 40, 42, 45, 50, 75]
        :return:
        """
        current, s, done = self.__root, [], False
        while not done:
            if current is not None:
                s.append(current)
                current = current.left
            else:
                if len(s):
                    current = s.pop()
                    print(current.value)
                    current = current.right
                else:
                    done = True

    def postorder_traverse(self):
        def postorder(node: Node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            print(node.value)

        postorder(self.__root)

    def postorder_traverse_iter(self):
        s1, s2 = [], []
        s1.append(self.__root)
        while len(s1):
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while len(s2):
            node = s2.pop()
            print(node.value)

    def levelorder_traverse(self):
        root, queue = self.__root, []
        if not root: return
        queue.append(root)
        while len(queue):
            temp = queue.pop(0)
            print(temp.value)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    # end def
# end class


class TestBinaryTree(unittest.TestCase):
    def test_preorder_traverse(self):
        c_root_node = construct_binary_tree_1()
        c_binary_tree = BinaryTree(c_root_node)
        self.assertEqual(c_binary_tree.preorder_traverse(),
                         [42, 41, 10, 40, 50, 45, 75])
    # end def


def construct_binary_tree_1() -> Node:
    root = Node(42)

    root.left = Node(41)
    root.right = Node(50)

    root.left.left = Node(10)
    root.left.right = Node(40)

    root.right.left = Node(45)
    root.right.right = Node(75)

    return root


root_node = construct_binary_tree_1()
binary_tree = BinaryTree(root_node)

# print('preorder traverse: ')
t1 = binary_tree.preorder_traverse()

# print('\npreorder traverse iterative: ')
t2 = binary_tree.preorder_traverse_iter()

preorder_implemented_correctly = 0

br = 1

# end of file
