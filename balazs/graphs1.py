
class GraphNode:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = None


def bfs(start_node: GraphNode):
    que = [start_node]
    while que:
        actual_node = que.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for neighbor in actual_node.adjacency_list:
            if not neighbor.visited:
                que.append(neighbor)


def one():
    node1 = GraphNode('1')
    node2 = GraphNode('2')
    node3 = GraphNode('3')
    node4 = GraphNode('4')
    node5 = GraphNode('5')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    bfs(node1)

one()






#
