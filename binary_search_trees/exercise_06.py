import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_search_trees.exercise_02 import AVLTreeMap
from linear_lists.exercise_01 import ArrayDeque


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def print_tree_vertical(root):

    if root is None:
        print("(árvore vazia)")
        return

    h = height(root)
    space_between = 2 ** h

    queue = ArrayDeque()
    queue.add_last(root)
    current_level = 1

    while not queue.is_empty() and current_level <= h:
        level_size = queue.size()
        line = " " * (space_between // 2)

        next_queue = ArrayDeque()
        for _ in range(level_size):
            node = queue.remove_first()

            if node is not None:
                line += str(node.element.key)
                next_queue.add_last(node.left)
                next_queue.add_last(node.right)
            else:
                line += " "
                next_queue.add_last(None)
                next_queue.add_last(None)

            line += " " * space_between

        print(line.rstrip())
        queue = next_queue
        space_between //= 2
        current_level += 1


if __name__ == "__main__":
    avl = AVLTreeMap()

    # --- Montagem manual da árvore da Figura 11.14b ---
    #                                   44
    #                    17                          62
    #                        32            50               78
    #                                     48   54                       88
    #
    n44 = avl._Item(44, 44); n44.height = 4
    n17 = avl._Item(17, 17); n17.height = 2
    n32 = avl._Item(32, 32); n32.height = 1
    n62 = avl._Item(62, 62); n62.height = 3
    n50 = avl._Item(50, 50); n50.height = 2
    n48 = avl._Item(48, 48); n48.height = 1
    n54 = avl._Item(54, 54); n54.height = 1
    n78 = avl._Item(78, 78); n78.height = 2
    n88 = avl._Item(88, 88); n88.height = 1

    root = avl._tree.add_root(n44)

    left_44 = avl._tree.add_left(root, n17)
    right_44 = avl._tree.add_right(root, n62)

    avl._tree.add_right(left_44, n32)

    node_50 = avl._tree.add_left(right_44, n50)
    node_78 = avl._tree.add_right(right_44, n78)

    avl._tree.add_left(node_50, n48)
    avl._tree.add_right(node_50, n54)

    avl._tree.add_right(node_78, n88)

    print("Árvore AVL antes da remoção da chave 62:\n")
    print_tree_vertical(avl._tree.root)

    print("\nRemovendo a chave 62...\n")
    removed = avl.remove(62)
    # removed = avl.remove(32)  # Pra ficar igual o da imagem mesmo
    print("valor removido:", removed, "\n")

    print("Árvore AVL depois da remoção da chave 62:\n")
    print_tree_vertical(avl._tree.root)
