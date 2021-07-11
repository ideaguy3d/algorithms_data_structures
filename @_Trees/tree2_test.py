'''
python3 -m unittest tree2_test.py
'''

import unittest
from tree2 import *


class Tree2Test(unittest.TestCase):
    def test_preorder_traverse(self):
        c_root_node = construct_binary_tree_1()
        c_binary_tree = BinaryTree(c_root_node)
        self.assertEqual(c_binary_tree.preorder_traverse(),
                         [42, 41, 10, 40, 50, 45, 75])


# end of file
