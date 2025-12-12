from exercise_12 import Node

def count_nodes_recursive(node):
    if node is None:
        return 0
    return 1 + count_nodes_recursive(node.next)

def build(vals):
    head=None; tail=None
    for v in vals:
        n=Node(v)
        if head is None: head=tail=n
        else: tail.next=n; tail=n
    return head

def main():
    h = build([1,2,3,4,5])
    print("count:", count_nodes_recursive(h))
    print("count empty:", count_nodes_recursive(None))

if __name__ == "__main__":
    main()
