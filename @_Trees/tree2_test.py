"""
    $ python3 -m unittest tree2_test.py
"""

import unittest
from tree2 import *


class Tree2Test(unittest.TestCase):
    def test_preorder_traverse(self):
        c_root_node = construct_binary_tree()
        c_binary_tree = BinaryTree(c_root_node)
        self.assertEqual(c_binary_tree.preorder_traverse(),
                         [42, 41, 10, 40, 50, 45, 75])


class TestBinaryTree(unittest.TestCase):
    def test_preorder_traverse(self):
        self.root_node = construct_binary_tree()
        self.binary_tree = BinaryTree(self.root_node, testing=True)
        _list = [42, 41, 10, 40, 50, 45, 75]
        self.assertEqual(self.binary_tree.preorder_traverse(), _list)
    # end def

    def test_inorder_traverse(self):
        self.root_node = construct_binary_tree()
        self.binary_tree = BinaryTree(self.root_node, testing=True)
        inorder_list_1 = [10, 41, 40, 42, 45, 50, 75]
        self.assertEqual(self.binary_tree.inorder_traverse(), inorder_list_1)
        self.assertEqual(self.binary_tree.inorder_traverse(),
                         self.binary_tree.inorder_traverse_iter())
    # end def


# end of file
