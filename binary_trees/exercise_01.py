class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None

class LinkedBinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def add_root(self, element):
        if self.root is not None:
            raise Exception("Root already exists")
        self.root = Node(element)
        return self.root

    def add_left(self, node, element):
        if node.left is not None:
            raise Exception("Left child already exists")
        n = Node(element)
        n.parent = node
        node.left = n
        return n

    def add_right(self, node, element):
        if node.right is not None:
            raise Exception("Right child already exists")
        n = Node(element)
        n.parent = node
        node.right = n
        return n

    def is_leaf(self, node):
        return node is not None and node.left is None and node.right is None
    
    def preorder(self):
        out = []
        self._preorder(self.root, out)
        return out

    def _preorder(self, node, out):
        if node is None:
            return
        out.append(node.element)
        self._preorder(node.left, out)
        self._preorder(node.right, out)

    def inorder(self):
        out = []
        self._inorder(self.root, out)
        return out

    def _inorder(self, node, out):
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.element)
        self._inorder(node.right, out)

    def postorder(self):
        out = []
        self._postorder(self.root, out)
        return out

    def _postorder(self, node, out):
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.element)

# small helper to build from nested tuple for tests: (val, left_tuple, right_tuple)
def build_from_tuple(tup):
    if tup is None:
        return None
    val = tup[0]
    left = tup[1] if len(tup) > 1 else None
    right = tup[2] if len(tup) > 2 else None
    root = Node(val)
    def build(node, lt, rt):
        if lt is not None:
            node.left = Node(lt[0])
            node.left.parent = node
            llt = lt[1] if len(lt) > 1 else None
            lrt = lt[2] if len(lt) > 2 else None
            build(node.left, llt, lrt)
        if rt is not None:
            node.right = Node(rt[0])
            node.right.parent = node
            rlt = rt[1] if len(rt) > 1 else None
            rrt = rt[2] if len(rt) > 2 else None
            build(node.right, rlt, rrt)
    build(root, left, right)
    return root
