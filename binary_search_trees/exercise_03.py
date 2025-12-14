import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from binary_search_trees.exercise_01 import TreeMap


RED = True
BLACK = False


class RBTreeMap(TreeMap):
    class _Item(TreeMap._Item):
        def __init__(self, key, value):
            super().__init__(key, value)
            self.color = RED  

    def _is_red(self, node):
        return node is not None and getattr(node.element, "color", BLACK) == RED

    def _set_color(self, node, color):
        if node is not None:
            node.element.color = color

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

    def _grandparent(self, node):
        return node.parent.parent if node and node.parent else None

    def _uncle(self, node):
        g = self._grandparent(node)
        if g is None:
            return None
        return g.right if node.parent is g.left else g.left

    def _sibling(self, node, parent):
        if parent is None:
            return None
        return parent.right if parent.left is node else parent.left

    def put(self, key, value):
        item = RBTreeMap._Item(key, value)
        if self._tree.root is None:
            self._tree.add_root(item)
            self._set_color(self._tree.root, BLACK)
            return

        node = self._search(self._tree.root, key)
        if node.element.key == key:
            node.element.value = value
            return

        if key < node.element.key:
            newn = self._tree.add_left(node, item)
        else:
            newn = self._tree.add_right(node, item)

        self._fix_insert(newn)

    def _fix_insert(self, node):
        while node.parent and self._is_red(node.parent):
            g = self._grandparent(node)
            if g is None:
                break
            if node.parent is g.left:
                u = g.right
                if self._is_red(u):
                    self._set_color(node.parent, BLACK)
                    self._set_color(u, BLACK)
                    self._set_color(g, RED)
                    node = g
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    self._set_color(node.parent, BLACK)
                    self._set_color(g, RED)
                    self._rotate_right(g)
            else:
                u = g.left
                if self._is_red(u):
                    self._set_color(node.parent, BLACK)
                    self._set_color(u, BLACK)
                    self._set_color(g, RED)
                    node = g
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    self._set_color(node.parent, BLACK)
                    self._set_color(g, RED)
                    self._rotate_left(g)
        self._set_color(self._tree.root, BLACK)

    def remove(self, key):
        if self._tree.root is None:
            return None
        node = self._search(self._tree.root, key)
        if node is None or node.element.key != key:
            return None

        removed_value = node.element.value

        if node.left and node.right:
            succ = node.right
            while succ.left:
                succ = succ.left
            node.element.key = succ.element.key
            node.element.value = succ.element.value
            node = succ  

        child = node.left if node.left else node.right
        parent = node.parent
        original_color = getattr(node.element, "color", BLACK)

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

        if original_color == BLACK:
            self._fix_delete(child, parent)

        return removed_value

    def _fix_delete(self, x, parent):

        while (x is None or not self._is_red(x)) and x is not self._tree.root:
            if parent is None:
                break
            sib = self._sibling(x, parent)
            if sib is None:
                x = parent
                parent = x.parent
                continue

            if self._is_red(sib):
                self._set_color(sib, BLACK)
                self._set_color(parent, RED)
                if parent.left is sib:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
                sib = self._sibling(x, parent)

            left_red = self._is_red(sib.left)
            right_red = self._is_red(sib.right)

            if not left_red and not right_red:
                self._set_color(sib, RED)
                x = parent
                parent = x.parent
                continue

            if parent.left is x:
                if not right_red and left_red:
                    self._set_color(sib.left, BLACK)
                    self._set_color(sib, RED)
                    self._rotate_right(sib)
                    sib = self._sibling(x, parent)
                self._set_color(sib, getattr(parent.element, "color", BLACK))
                self._set_color(parent, BLACK)
                self._set_color(sib.right, BLACK)
                self._rotate_left(parent)
                x = self._tree.root
                break
            else:
                if not left_red and right_red:
                    self._set_color(sib.right, BLACK)
                    self._set_color(sib, RED)
                    self._rotate_left(sib)
                    sib = self._sibling(x, parent)
                self._set_color(sib, getattr(parent.element, "color", BLACK))
                self._set_color(parent, BLACK)
                self._set_color(sib.left, BLACK)
                self._rotate_right(parent)
                x = self._tree.root
                break

        if x is not None:
            self._set_color(x, BLACK)
