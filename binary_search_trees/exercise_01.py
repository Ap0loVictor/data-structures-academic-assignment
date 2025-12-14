import sys, os
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

    def _search(self, node, key):
        if node is None or node.element.key == key:
            return node
        if key < node.element.key:
            return self._search(node.left, key) if node.left else node
        else:
            return self._search(node.right, key) if node.right else node

    def _subtree_min(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def get(self, key):
        if self._tree.root is None:
            return None
        node = self._search(self._tree.root, key)
        return node.element.value if node and node.element.key == key else None

    def put(self, key, value):
        item = TreeMap._Item(key, value)
        if self._tree.root is None:
            self._tree.add_root(item)
            return
        node = self._search(self._tree.root, key)
        if node.element.key == key:
            node.element.value = value
        else:
            if key < node.element.key:
                self._tree.add_left(node, item)
            else:
                self._tree.add_right(node, item)

    def remove(self, key):
        if self._tree.root is None:
            return None
        node = self._search(self._tree.root, key)
        if node is None or node.element.key != key:
            return None

        removed = node.element.value

        if node.left and node.right:
            succ = self._subtree_min(node.right)
            node.element = succ.element
            node = succ

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

        return removed
