class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def build(vals):
    h = None; t = None
    for v in vals:
        n = Node(v)
        if h is None:
            h = t = n
        else:
            t.next = n; t = n
    return h

def to_list(head):
    a = []
    cur = head
    while cur:
        a.append(cur.data); cur = cur.next
    return a

def main():
    h = build([1,2,3,4])
    print("orig:", to_list(h))
    h = reverse_recursive(h)
    print("reversed:", to_list(h))

if __name__ == "__main__":
    main()
