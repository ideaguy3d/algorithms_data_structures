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


class BinarySearchTree(BinaryTree):
    tree: Union[Node, Any]

    def __init__(self):
        super().__init__()
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


class AVL_Tree(BinarySearchTree):
    def __init__(self, value):
        super().__init__()
        self.left = AVL_Tree
        self.right = Union[AVL_Tree, None]
        self.value = value
        self.depth = 1

    def set_depth_based_on_children(self):
        if self.node is None:
            self.depth = 0
        else:
            self.depth = 1

        if self.left is not None:
            self.depth = self.left.depth + 1

        if self.right is not None and self.depth <= self.right.depth:
            self.depth = self.right.depth + 1

    def rotateLL(self):
        value_before = self.value
        right_before = self.right
        self.value = self.left.value

        self.right = self.left
        self.left = self.left.left
        self.right.left = self.right.right
        self.right.right = right_before
        self.right.value = value_before

        self.right.get_depth_from_children()
        self.get_depth_from_children()

    def rotateRR(self):
        value_before, left_before = self.value, self.left
        self.value = self.right.value

        self.right = self.left
        self.right = self.right.right
        self.left.right = self.left.left
        self.left.left = left_before
        self.left.value = value_before

        self.left.update_in_new_location()
        self.update_in_new_location()

    def balance(self):
        ldepth = 0 if self.left is None else self.left.depth
        rdepth = 0 if self.right is None else self.right.depth
        if ldepth > rdepth + 1:
            lldepth = 0 if self.left.left is None else self.left.left.depth
            lrdepth = 0 if self.left.right is None else self.left.right.depth
            if lldepth < lrdepth:
                self.left.rotateRR()
            self.rotateLL()
        elif ldepth + 1 < rdepth:
            rrdepth = 0 if self.right.right is None else self.right.right.depth
            rldepth = 0 if self.right.left is None else self.right.left.depth
            if rrdepth < rldepth:
                self.right.rotateLL()
            self.rotateRR()

    def insert(self, value) -> bool:
        child_inserted = False
        if value == self.value:
            return False
        elif value < self.value:
            if self.left is None:
                self.left = AVL_Tree(value)
                child_inserted = True
            else:
                # recursive call
                child_inserted = self.left.insert(value)
                if child_inserted: self.balance()
        elif value > self.value:
            if self.right is None:
                self.right = AVL_Tree(value)
                child_inserted = True
            else:
                # recursive call
                child_inserted = self.right.insert(value)
                if child_inserted: self.balance()
        if child_inserted: self.set_depth_based_on_children()
        return child_inserted

    def remove(self, value):
        def find_min(root):
            while root.left: root = root.left
            return root

        def delete_recursive(root, c_value):
            if not root:
                return None
            elif value < c_value:
                root.left = delete_recursive(root.left, value)
            elif value > c_value:
                root.right = delete_recursive(root.right, value)
            else:  # no children
                if not root.left and not root.right:
                    return None  # case 1
                elif not root.left:
                    root = root.right
                    return root
                elif not root.left:
                    root = root.right
                    return root
                else:
                    temp = find_min(root.right)
                    root.value = temp.value
                    root.right = delete_recursive(root.right, temp.value)
                    return root
            root.update_in_new_location()
            return root

        return delete_recursive(self, value)


# ~ Utilility Functions ~ #
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


def construct_avl_tree():
    avl = AVL_Tree(1)
    a_set = [2, 3, 4, 5, 123, 203, 2222]
    for i in a_set:
        avl.insert(i)
    print(avl)
    br = 1


construct_avl_tree()


def run_binary_tree():
    binary_search_tree = construct_binary_search_tree()
    find20 = binary_search_tree.find_node(20)
    find42 = binary_search_tree.find_node(42)

    root_node = construct_binary_tree()
    binary_tree = BinaryTree(root_node)

    # print('preorder traverse: ')
    t1 = binary_tree.preorder_traverse()

    # print('\npreorder traverse iterative: ')
    t2 = binary_tree.preorder_traverse_iter()

    br = 1





# end of file
