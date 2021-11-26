package java_recap;

import org.junit.Test;

//       3
//    /    \
//   2      5
//  / \    / \
// 1   N  4   6
public class BinaryTree {

    Node root;

    public void add(int value) {
        root = addRecursive(root, value);
    }

    public boolean containsNode(int value) {
        return containsNodeRecursive(root, value);
    }

    public void delete(int value) {
        root = deleteRecursive(root, value);
    }

    private Node addRecursive(Node current, int value) {
        if (current == null) {
            return new Node(value);
        }

        if (value < current.value) {
            current.left = addRecursive(current.left, value);
        } else if (value > current.value) {
            current.right = addRecursive(current.right, value);
        } else {
            // value already exists
            return current;
        }

        return current;
    }

    private BinaryTree createBinaryTree() {
        BinaryTree bt = new BinaryTree();
        bt.add(6);
        bt.add(4);
        bt.add(8);
        bt.add(3);
        bt.add(5);
        bt.add(7);
        bt.add(9);

        return bt;
    }

    private boolean containsNodeRecursive(Node current, int value) {
        if (current == null || value == 0) {
            return false;
        }

        if (value == current.value) {
            return true;
        }

        return (value < current.value ? containsNodeRecursive(current.left, value)
                : containsNodeRecursive(current.right, value));
    }

    private Node deleteRecursive(Node current, int value) {
        if (current == null) {
            return null;
        }

        if (current.value == value) {
            // delete node
            // 1. node has no children
            if (current.left == null && current.right == null) {
                return null;
            }
            // 2. node has exactly one child
            if (current.left == null) {
                return current.right;
            }
            if (current.right == null) {
                return current.left;
            }
            // 3. node has two children
            // find smallest value
            int smallestValue = findSmallestValue(current.right);
            current.value = smallestValue;
            current.right = deleteRecursive(current.right, smallestValue);
            return current;
        }
        if (value < current.value) {
            current.left = deleteRecursive(current.left, value);
        } else if (value > current.value) {
            current.right = deleteRecursive(current.right, value);
        }

        return current;
    }

    private int findSmallestValue(Node root) {
        return root.left == null ? root.value : findSmallestValue(root.left);
    }

    @Test
    public void checkIfNodeExist_GivenABinaryTree() {
        BinaryTree bt = new BinaryTree();
        assertTrue(bt.containsNode(6));
        assertTrue(bt.containsNode(4));

        assertFalse(bt.containsNode(1));

    }

    @Test
    public void givenABinaryTree_WhenAddingElements_ThenTreeContainsThoseElements() {
        BinaryTree bt = createBinaryTree();

        assertTrue(bt.containsNode(6));
        assertTrue(bt.containsNode(4));

        assertFalse(bt.containsNode(1));
    }

}
