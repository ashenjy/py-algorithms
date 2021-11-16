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
        pass

    # is binary search tree
    def is_bst(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    # tuple to Tree Node Obj

    @staticmethod
    def parse_tuple(tuple):
        pass
