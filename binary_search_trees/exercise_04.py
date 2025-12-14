import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_search_trees.exercise_01 import TreeMap
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
                # adiciona filhos (podem ser None para preservar posição)
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
    tree = TreeMap()
    keys = [30, 40, 24, 58, 48, 26, 11, 13]

    for k in keys:
        tree.put(k, k)
        print(f"\nApós inserir {k}:")
        print_tree_vertical(tree._tree.root)
