from exercise_01 import LinkedBinaryTree


def _transform_sum_subtrees(node):

    if node is None:
        return 0

    left_sum = _transform_sum_subtrees(node.left)
    right_sum = _transform_sum_subtrees(node.right)

    original_value = node.element

    node.element = left_sum + right_sum

    return original_value + left_sum + right_sum


def transform_tree_to_sum_subtrees(tree):
    if tree is None or tree.root is None:
        return
    _transform_sum_subtrees(tree.root)


def main():
    # Árvore do exemplo do enunciado
    #
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    4   5   6
    #       / \
    #      7   8
    #
    T = LinkedBinaryTree()
    r = T.add_root(1)
    n2 = T.add_left(r, 2)
    n3 = T.add_right(r, 3)
    T.add_left(n2, 4)
    n5 = T.add_left(n3, 5)
    T.add_right(n3, 6)
    T.add_left(n5, 7)
    T.add_right(n5, 8)

    print("Preorder ANTES da transformação:")
    print(T.preorder())
    print()

    transform_tree_to_sum_subtrees(T)

    print("Preorder DEPOIS da transformação:")
    print(T.preorder())
    print()

    print("Inorder após transformação:")
    print(T.inorder())

    print("\nPostorder após transformação:")
    print(T.postorder())


if __name__ == "__main__":
    main()
