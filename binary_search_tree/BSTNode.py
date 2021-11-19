class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    @staticmethod
    def insert(root, key, value):
        if root is None:
            root = BSTNode(key, value)
        elif key < root.key:
            root.left = BSTNode.insert(root.left, key, value)
            root.left.parent = root
        elif key > root.key:
            root.right = BSTNode.insert(root.right, key, value)
            root.right.parent = root
        return root

    @staticmethod
    def find(tree, username):
        if tree is None:
            return None

        if username == tree.key:
            return tree
        elif username < tree.key:
            return BSTNode.find(tree.left, username)
        else:
            return BSTNode.find(tree.right, username)

    @staticmethod
    def update(tree, user):
        if tree is None or user is None:
            return None
        target = BSTNode.find(tree, user.username)

        if target is None:
            return None
        else:
            target.value = user
        return

    def list_all(self):
        if self is None or self.key is None:
            return []
        return (BSTNode.list_all(self.left) + [(self.key, self.value)] + BSTNode.list_all(self.right))

    @staticmethod
    def display(tree, space='\t', level=0):
        if tree is None:
            print(space * level + "None")
            return

        if tree.left is None and tree.right is None:
            print(space * level + str(tree.key))
            return

        BSTNode.display(tree.left, space, level + 1)
        print(space * level + str(tree.key))
        BSTNode.display(tree.right, space, level + 1)

    def tree_size(self):
        pass

    def __len__(self):
        pass
