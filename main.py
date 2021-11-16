from binary_tree.Node import Node


def main():
    #          2
    #    3            5
    # 1     n      3      7
    #            n   4  6    8
    #
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

    # convert tuple to Tree Node Object
    node = Node.parse_tuple(tree_tuple)

    node

    node.display_keys('     ')
    node.max_depth()
    node.min_depth()
    node.size()
    node.diameter()
    node.is_bst()


if __name__ == '__main__':
    main()
