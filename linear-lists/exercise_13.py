class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def penultimate(head):
    if head is None or head.next is None:
        return None
    cur = head
    while cur.next and cur.next.next:
        cur = cur.next
    return cur  

def build_list(vals):
    head = None
    tail = None
    for v in vals:
        n = Node(v)
        if head is None:
            head = tail = n
        else:
            tail.next = n
            tail = n
    return head

def main():
    h = build_list([1,2,3,4])
    p = penultimate(h)
    print("penultimate of [1,2,3,4] ->", p.data if p else None)
    h = build_list([1])
    print("penultimate of [1] ->", penultimate(h))

if __name__ == "__main__":
    main()
