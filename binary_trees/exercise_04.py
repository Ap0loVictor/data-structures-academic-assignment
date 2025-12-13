from exercise_01 import LinkedBinaryTree, Node


def nodes_identical(n1, n2) -> bool:
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    if n1.element != n2.element:
        return False
    return nodes_identical(n1.left, n2.left) and nodes_identical(n1.right, n2.right)


def trees_identical(t1, t2) -> bool:
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return nodes_identical(t1.root, t2.root)


def main():
    T1 = LinkedBinaryTree()
    r = T1.add_root(1)
    n2 = T1.add_left(r, 2)
    n3 = T1.add_right(r, 3)
    T1.add_left(n2, 4)
    T1.add_right(n2, 5)
    n6 = T1.add_left(n3, 6)
    n7 = T1.add_right(n3, 7)
    T1.add_left(n6, 8)
    T1.add_right(n7, 9)

    T2 = LinkedBinaryTree()
    r2 = T2.add_root(1)
    a2 = T2.add_left(r2, 2)
    b2 = T2.add_right(r2, 3)
    T2.add_left(a2, 4)
    T2.add_right(a2, 5)
    c2 = T2.add_left(b2, 6)
    d2 = T2.add_right(b2, 7)
    T2.add_left(c2, 8)
    T2.add_right(d2, 9)

    T3 = LinkedBinaryTree()
    r3 = T3.add_root(1)
    x2 = T3.add_left(r3, 2)
    y2 = T3.add_right(r3, 3)
    T3.add_left(x2, 4)
    T3.add_right(x2, 999)   # valor diferente aqui
    z2 = T3.add_left(y2, 6)
    w2 = T3.add_right(y2, 7)
    T3.add_left(z2, 8)
    T3.add_right(w2, 9)

    print("Teste exercício 4 — verificar árvores idênticas")
    print("T1 == T2 ?", trees_identical(T1, T2))  
    print("T1 == T3 ?", trees_identical(T1, T3))  

    # testes com None
    print("T1 == None ?", trees_identical(T1, None))  
    print("None == None ?", trees_identical(None, None)) 


if __name__ == "__main__":
    main()
