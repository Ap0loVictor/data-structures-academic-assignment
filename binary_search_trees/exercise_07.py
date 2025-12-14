import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_search_trees.exercise_03 import RBTreeMap
from linear_lists.exercise_01 import ArrayDeque


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def _node_label(node):

    if node is None:
        return " "
    key = node.element.key
    color = getattr(node.element, "color", False)  
    c = "R" if color else "B"
    return f"{key}({c})"


def print_tree_vertical(root):

    if root is None:
        print("(árvore vazia)")
        return

    h = height(root)
    space_between = 2 ** h

    queue = ArrayDeque()
    queue.add_last(root)
    current_level = 1
    max_levels = h

    while not queue.is_empty() and current_level <= max_levels:
        level_size = queue.size()
        line = " " * (space_between // 2)

        next_queue = ArrayDeque()
        for _ in range(level_size):
            node = queue.remove_first()

            label = _node_label(node)
            line += label

            if node is None:
                next_queue.add_last(None)
                next_queue.add_last(None)
            else:
                next_queue.add_last(node.left)
                next_queue.add_last(node.right)

            line += " " * space_between

        print(line.rstrip())
        queue = next_queue
        space_between //= 2
        current_level += 1


if __name__ == "__main__":
    rbt = RBTreeMap()

    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]

    for k in keys:
        rbt.put(k, k)
        print(f"\nApós inserir {k}:")
        print_tree_vertical(rbt._tree.root)
