from typing import Tuple


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def display_keys(self, space='\t', level=0):
        if self.key is None:
            print(space * level + "None")
            return

        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        Node.display_keys(self.left, space, level + 1)
        print(space * level + str(self.key))
        Node.display_keys(self.right, space, level + 1)

    def max_depth(self):
        if self is None:
            return 0
        return 1 + max(Node.max_depth(self.left), Node.max_depth(self.right))

    def min_depth(self):
        if self is None:
            return 0
        return 1 + min(Node.max_depth(self.left), Node.max_depth(self.right))

    def diameter(self):
        return self.max_depth

    # no of nodes
    def size(self):
        return len(self.traverse_in_order())

    # left, root, right
    def traverse_in_order(self):
        if self is None or self.key is None:
            return []

        return (Node.traverse_in_order(self.left) + [self.key] + Node.traverse_in_order(self.right))

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
