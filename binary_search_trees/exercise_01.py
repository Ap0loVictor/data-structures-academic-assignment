import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_trees.exercise_01 import LinkedBinaryTree


class TreeMap:
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self._tree = LinkedBinaryTree()

    def _subtree_search(self, node, key):
        if node is None:
            return None
        if key == node.element.key:
            return node
        if key < node.element.key:
            if node.left is None:
                return node
            return self._subtree_search(node.left, key)
        else:
            if node.right is None:
                return node
            return self._subtree_search(node.right, key)

    def _subtree_min(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def get(self, key):
        if self._tree.root is None:
            return None
        node = self._subtree_search(self._tree.root, key)
        if node.element.key == key:
            return node.element.value
        return None

    def put(self, key, value):
        item = TreeMap._Item(key, value)

        if self._tree.root is None:
            self._tree.add_root(item)
            return

        node = self._subtree_search(self._tree.root, key)

        if node.element.key == key:
            node.element.value = value
        elif key < node.element.key:
            self._tree.add_left(node, item)
        else:
            self._tree.add_right(node, item)

    def remove(self, key):
        if self._tree.root is None:
            return None

        node = self._subtree_search(self._tree.root, key)
        if node.element.key != key:
            return None

        removed_value = node.element.value

        if node.left is not None and node.right is not None:
            succ = self._subtree_min(node.right)
            node.element = succ.element
            node = succ

        child = node.left if node.left is not None else node.right
        parent = node.parent

        if parent is None:
            self._tree.root = child
            if child is not None:
                child.parent = None
        else:
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
            if child is not None:
                child.parent = parent

        return removed_value
