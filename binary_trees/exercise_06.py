from exercise_01 import LinkedBinaryTree, Node

def _collect_paths_from_node(node, path, out):
    
    if node is None:
        return

    path.append(node.element)

    if node.left is None and node.right is None:
        out.append(list(path)) 
    else:
        _collect_paths_from_node(node.left, path, out)
        _collect_paths_from_node(node.right, path, out)

    path.pop()


def root_to_leaf_paths(tree_or_node):

    root = None
    if tree_or_node is None:
        return []
    if isinstance(tree_or_node, LinkedBinaryTree):
        root = tree_or_node.root
    else:
        root = tree_or_node

    out = []
    _collect_paths_from_node(root, [], out)
    return out


def print_root_to_leaf_paths(tree_or_node):

    paths = root_to_leaf_paths(tree_or_node)
    for p in paths:
        print(" -> ".join(str(x) for x in p))


def main():
    T = LinkedBinaryTree()
    r = T.add_root(1)
    n2 = T.add_left(r, 2)
    n3 = T.add_right(r, 3)
    T.add_left(n2, 4)
    T.add_right(n2, 5)
    n6 = T.add_left(n3, 6)
    n7 = T.add_right(n3, 7)
    T.add_left(n6, 8)
    T.add_right(n7, 9)

    print("=== Caminhos raiz->folha ===")
    print_root_to_leaf_paths(T)

    print("\n=== More tests ===")
    empty = LinkedBinaryTree()  
    print("Árvore vazia ->", root_to_leaf_paths(empty)) 
    print_root_to_leaf_paths(empty)

    single = LinkedBinaryTree()
    single.add_root(42)
    print("Árvore com apenas raiz ->", root_to_leaf_paths(single)) 
    print_root_to_leaf_paths(single)



if __name__ == "__main__":
    main()
