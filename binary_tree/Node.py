from typing import Tuple


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def display_keys(self, space='\t', level=0):
        pass

    def max_depth(self):
        pass

    def min_depth(self):
        pass

    def diameter(self):
        pass

    def size(self):
        pass

    # tree to tuple
    def to_tuple(self):
        if self is None:
            return None

        if self.left is None and self.right is None:
            return self.key

        return (Node.to_tuple(self.left), self.key, Node.to_tuple(self.right))

    # is binary search tree
    def is_bst(self):
        pass

    def __repr__(self):
        return "Binary Tree: < {} >".format(self.to_tuple())

    def __str__(self):
        return "Binary Tree: < {} >".format(self.to_tuple())

    # tuple to Tree Node Obj
    # ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    @staticmethod
    def parse_tuple(tuple):
        if tuple is None:
            node = None
        if isinstance(tuple, Tuple) and len(tuple) == 3:
            # print(f"parse_tuple().tuple exist: {tuple}")
            node = Node(tuple[1])  # key
            node.left = Node.parse_tuple(tuple[0])
            node.right = Node.parse_tuple(tuple[2])
        else:
            node = Node(tuple)
        # print(Node.to_tuple(node))
        return node
