import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from exercise_01 import LinkedBinaryTree
from linear_lists.exercise_01 import ArrayDeque


def find_node_by_value(root, value):
    if root is None:
        return None
    if root.element == value:
        return root
    left = find_node_by_value(root.left, value)
    if left is not None:
        return left
    return find_node_by_value(root.right, value)


def ancestors_of_value(tree, value):
    if tree is None:
        return []
    root = tree.root
    target = find_node_by_value(root, value)
    if target is None:
        return []
    res = []
    current = target.parent
    while current is not None:
        res.append(current.element)
        current = current.parent
    return res


def ancestors_nodes_of_index(tree, index, order="level"):
    if tree is None:
        return []
    target = find_node_by_index(tree, index, order)
    if target is None:
        return []
    res = []
    cur = target.parent
    while cur is not None:
        res.append(cur)
        cur = cur.parent
    return res


def find_node_by_index(tree_or_root, index, order="level"):
    if index < 1:
        return None

    root = tree_or_root.root if isinstance(tree_or_root, LinkedBinaryTree) else tree_or_root
    if root is None:
        return None

    i = 0
    for node in _traverse_nodes(root, order):
        i += 1
        if i == index:
            return node
    return None  

def _traverse_nodes(root, order):

    if root is None:
        return

    if order == "level":
        q = ArrayDeque()
        q.add_last(root)

        while not q.is_empty():
            node = q.remove_first()
            yield node

            if node.left is not None:
                q.add_last(node.left)
            if node.right is not None:
                q.add_last(node.right)
        return

    if order == "preorder":
        yield root
        if root.left is not None:
            yield from _traverse_nodes(root.left, order)
        if root.right is not None:
            yield from _traverse_nodes(root.right, order)

    elif order == "inorder":
        if root.left is not None:
            yield from _traverse_nodes(root.left, order)
        yield root
        if root.right is not None:
            yield from _traverse_nodes(root.right, order)

    elif order == "postorder":
        if root.left is not None:
            yield from _traverse_nodes(root.left, order)
        if root.right is not None:
            yield from _traverse_nodes(root.right, order)
        yield root

    else:
        raise ValueError("order inválida")


    if order == "preorder":
        yield root
        if root.left is not None:
            for x in _traverse_nodes(root.left, order):
                yield x
        if root.right is not None:
            for x in _traverse_nodes(root.right, order):
                yield x
    elif order == "inorder":
        if root.left is not None:
            for x in _traverse_nodes(root.left, order):
                yield x
        yield root
        if root.right is not None:
            for x in _traverse_nodes(root.right, order):
                yield x
    elif order == "postorder":
        if root.left is not None:
            for x in _traverse_nodes(root.left, order):
                yield x
        if root.right is not None:
            for x in _traverse_nodes(root.right, order):
                yield x
        yield root
    else:
        raise ValueError("order must be one of: 'level','preorder','inorder','postorder'")


def main():
    T = LinkedBinaryTree()
    r = T.add_root(1)           
    n2 = T.add_left(r, 2)        
    n3 = T.add_right(r, 3)      
    T.add_left(n2, 4)           
    n5 = T.add_right(n2, 5)     
    n6 = T.add_left(n3, 6)      
    n7 = T.add_right(n3, 7)     
    T.add_left(n6, 8)           
    T.add_right(n7, 9)          

    print("Ancestrais do nó com valor 9:", ancestors_of_value(T, 9))  
    print("Ancestrais do nó com valor 6:", ancestors_of_value(T, 6))  
    print("Ancestrais do nó com valor 5:", ancestors_of_value(T, 5))  

    print("Ancestrais do nó 1 (raiz):", ancestors_of_value(T, 1))    
    print("Ancestrais de valor não presente:", ancestors_of_value(T, 999)) 

    print("Ancestrais do 9º nó (index=9, level-order):", [n.element for n in ancestors_nodes_of_index(T, 9, "level")])
    # Observação:
    # Nos testes acima, a função ancestors_of_value procura o nó a partir do
    # VALOR armazenado no nó (element). Ou seja, ela retorna os ancestrais do
    # nó que contém o valor informado.
    #
    # Já a função ancestors_nodes_of_index funciona de forma diferente:
    # ela considera a POSIÇÃO do nó na árvore segundo uma ordem de percurso
    # (neste caso, level-order). Assim, "9º nó" significa o nono nó visitado
    # durante o percurso, e não o nó cujo valor é 9.
    # Fiz assim, pois não sabia de qual forma o professor queria. 

if __name__ == "__main__":
    main()
