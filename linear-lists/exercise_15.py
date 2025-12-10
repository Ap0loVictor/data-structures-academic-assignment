class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes_recursive(node):
    if node is None:
        return 0
    return 1 + count_nodes_recursive(node.next)

def build(vals):
    h = None; t = None
    for v in vals:
        n = Node(v)
        if h is None:
            h = t = n
        else:
            t.next = n; t = n
    return h

def main():
    h = build([1,2,3,4,5])
    print("count:", count_nodes_recursive(h))
    print("count empty:", count_nodes_recursive(None))

if __name__ == "__main__":
    main()
