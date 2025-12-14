# exercise_02.py  (binary_search_trees)

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_trees.exercise_01 import LinkedBinaryTree


class AVLTreeMap:
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.height = 1

    def __init__(self):
        self._tree = LinkedBinaryTree()

    # -------- utilitários mínimos --------

    def _h(self, node):
        return node.element.height if node is not None else 0

    def _update(self, node):
        node.element.height = 1 + max(self._h(node.left), self._h(node.right))

    def _balance(self, node):
        return self._h(node.left) - self._h(node.right)

    def _search(self, node, key):
        if node is None or node.element.key == key:
            return node
        if key < node.element.key:
            return self._search(node.left, key) if node.left else node
        return self._search(node.right, key) if node.right else node

    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        if y.left:
            y.left.parent = z
        y.left = z

        parent = z.parent
        z.parent = y

        if parent is None:
            self._tree.root = y
            y.parent = None
        else:
            if parent.left is z:
                parent.left = y
            else:
                parent.right = y
            y.parent = parent

        self._update(z)
        self._update(y)

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        if y.right:
            y.right.parent = z
        y.right = z

        parent = z.parent
        z.parent = y

        if parent is None:
            self._tree.root = y
            y.parent = None
        else:
            if parent.left is z:
                parent.left = y
            else:
                parent.right = y
            y.parent = parent

        self._update(z)
        self._update(y)

    def _rebalance(self, node):
        while node:
            self._update(node)
            b = self._balance(node)

            if b > 1:
                if self._balance(node.left) < 0:
                    self._rotate_left(node.left)
                self._rotate_right(node)

            elif b < -1:
                if self._balance(node.right) > 0:
                    self._rotate_right(node.right)
                self._rotate_left(node)

            node = node.parent


    def get(self, key):
        if self._tree.root is None:
            return None
        node = self._search(self._tree.root, key)
        return node.element.value if node and node.element.key == key else None

    def put(self, key, value):
        item = AVLTreeMap._Item(key, value)

        if self._tree.root is None:
            self._tree.add_root(item)
            return

        node = self._search(self._tree.root, key)

        if node.element.key == key:
            node.element.value = value
            self._rebalance(node)
        else:
            if key < node.element.key:
                new = self._tree.add_left(node, item)
            else:
                new = self._tree.add_right(node, item)
            self._rebalance(new.parent)

    def remove(self, key):
        if self._tree.root is None:
            return None

        node = self._search(self._tree.root, key)
        if node.element.key != key:
            return None

        removed = node.element.value

        if node.left and node.right:
            s = node.right
            while s.left:
                s = s.left
            node.element = s.element
            node = s

        child = node.left if node.left else node.right
        parent = node.parent

        if parent is None:
            self._tree.root = child
            if child:
                child.parent = None
        else:
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
            if child:
                child.parent = parent

        self._rebalance(parent)
        return removed
