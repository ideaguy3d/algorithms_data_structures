
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


class Stack:
    def __init__(self):
        self.list = list()

    def pop(self):
        return self.list.pop()

    def push(self, value):
        self.list.append(value)

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"


def tree_practice():
    tree = Tree('apple')
    stack = Stack()
    visit_order = list()

    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))


def check_stack():
    stack = Stack()
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    stack.push("dates")
    print(stack.pop())
    print("\n")
    print(stack)

debug = 1





# end of file