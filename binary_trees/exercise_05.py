from exercise_01 import LinkedBinaryTree, Node


def _check_sum_node(node):
    if node is None:
        return True, 0

    if node.left is None and node.right is None:
        return True, node.element

    left_ok, left_sum = _check_sum_node(node.left)
    right_ok, right_sum = _check_sum_node(node.right)

    node_ok = (left_ok and right_ok and (node.element == left_sum + right_sum))

    total_sum = node.element + left_sum + right_sum

    return node_ok, total_sum


def is_sum_tree(tree):
    if tree is None:
        return True
    root = tree.root
    ok, _ = _check_sum_node(root)
    return ok


def main():
    T1 = LinkedBinaryTree()
    r = T1.add_root(44)
    n9 = T1.add_left(r, 9)
    n13 = T1.add_right(r, 13)
    T1.add_left(n9, 4)
    T1.add_right(n9, 5)
    T1.add_left(n13, 6)
    T1.add_right(n13, 7)

    print("Exemplo 1:", is_sum_tree(T1)) 

    T2 = LinkedBinaryTree()
    r2 = T2.add_root(44)
    a2 = T2.add_left(r2, 9)
    b2 = T2.add_right(r2, 13)
    T2.add_left(a2, 4)
    T2.add_right(a2, 5)
    T2.add_left(b2, 6)
    T2.add_right(b2, 999) 

    print("Exemplo 2:", is_sum_tree(T2))  

    T3 = LinkedBinaryTree()  
    print("Exemplo 3 (árvore vazia):", is_sum_tree(T3)) 

    T4 = LinkedBinaryTree()
    T4.add_root(5)
    print("Exemplo 4 (apenas raiz folha):", is_sum_tree(T4))  


if __name__ == "__main__":
    main()
