import unittest
from typing import Any, Union


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def output(value):
    if not BinaryTree.testing:
        print(value)


class BinaryTree:
    testing = False

    def __init__(self, c_root_node, testing=False):
        self.__root = c_root_node
        self.testing = testing

    def preorder_traverse(self):
        def preorder(node: Node):
            if not node: return
            _list.append(node.value)
            output(node.value)
            preorder(node.left)
            preorder(node.right)

        _list = []
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

    def inorder_traverse(self) -> list:
        def inorder(node: Node):
            if not node: return
            inorder(node.left)
            _list.append(node.value)
            if not self.testing: print(node.value)
            inorder(node.right)

        _list = []
        inorder(self.__root)
        return _list

    def inorder_traverse_iter(self):
        """
        result_1 = [10, 41, 40, 42, 45, 50, 75]
        :return:
        """
        current, stack, done, _list = self.__root, [], False, []
        while not done:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack):
                    current = stack.pop()
                    _list.append(current.value)
                    if not self.testing: print(current.value)
                    current = current.right
                else:
                    done = True
        return _list

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


class BinarySearchTree:
    tree: Union[Node, Any]

    def __init__(self):
        self.__root = None

    def insert(self, value):
        this_node = Node(value)
        if not self.__root:
            self.__root = this_node
        else:
            current_root = self.__root
            while True:
                if current_root.value > value:
                    if current_root.left is not None:
                        current_root = current_root.left
                    else:
                        current_root.left = this_node
                        break
                elif current_root.value < value:
                    if current_root.right is not None:
                        current_root = current_root.right
                    else:
                        current_root.right = this_node
                        break
                else:
                    break  # both are the same
    # end insert

    def remove(self, value: int) -> Node:
        def find_min(root: Node) -> Node:
            while root.left:
                root = root.left
            return root

        def delete_recursive(root: Node, c_value: int) -> Union[Node, None]:
            if not root:
                return None
            elif c_value < root.value:
                root.left = delete_recursive(root.left, c_value)
            elif c_value > root.value:
                root.right = delete_recursive(root.right, c_value)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left:
                    root = root.right
                    return root
                elif not root.right:
                    root = root.left
                    return root
                else:
                    temp = find_min(root.right)
                    root.value = temp.value
                    root.right = delete_recursive(root.right, c_value)
                    return root
            return root

        return delete_recursive(self.__root, value)
    # end remove

    def find_node(self, value: int) -> bool:
        current_root, found = self.__root, False
        while current_root:
            if value < current_root.value:
                current_root = current_root.left
            elif value > current_root.value:
                current_root = current_root.right
            else:  # we found a match
                found = True
                break
        return found

    def get_structure(self):
        return self.__root


def construct_binary_tree() -> Node:
    root = Node(42)

    root.left = Node(41)
    root.right = Node(50)

    root.left.left = Node(10)
    root.left.right = Node(40)

    root.right.left = Node(45)
    root.right.right = Node(75)

    return root


def construct_binary_search_tree() -> BinarySearchTree:
    _list = [42, 41, 10, 40, 50, 45, 75]
    bst = BinarySearchTree()
    for i in _list:
        bst.insert(i)
    return bst


unit_testing = False
if not unit_testing:
    binary_search_tree = construct_binary_search_tree()
    find20 = binary_search_tree.find_node(20)
    find42 = binary_search_tree.find_node(42)
    br2 = 1

    def run_binary_tree():
        root_node = construct_binary_tree()
        binary_tree = BinaryTree(root_node)

        # print('preorder traverse: ')
        t1 = binary_tree.preorder_traverse()

        # print('\npreorder traverse iterative: ')
        t2 = binary_tree.preorder_traverse_iter()

        preorder_implemented_correctly = 0

        br = 1

# end of file
