from binary_tree.Node import Node


def binary_tree(tuple):
    if tuple:
        # convert tuple to Tree
        node = Node.parse_tuple(tuple)
        print(node.__str__)

        if node:
            node.display_keys()
            print("IN ORDER TRAVERSAL :", node.traverse_in_order())
            print("MAX DEPTH :", node.max_depth())
            print("MiN DEPTH :", node.min_depth())
            # node.size()
            # node.diameter()
            # node.is_bst()
            # node.to_tuple()
            pass
        else:
            print(f"Tree found None! Invalid Tuple passed!")


if __name__ == '__main__':
    tuple_list = []

    #          2
    #    3            5
    # 1     n      3      7
    #            n   4  6    8
    #

    # test scenarios
    test_tuple1 = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    test_tuple2 = (2)
    test_tuple3 = (1, 2)  # invalid

    tuple_list.append(test_tuple1)
    # tuple_list.append(test_tuple2)
    # tuple_list.append(test_tuple3)

    for test_no, tuple in enumerate(tuple_list):
        binary_tree(tuple)
        print(f"TEST {test_no}: TUPLE <{tuple}> ===> Finished")
