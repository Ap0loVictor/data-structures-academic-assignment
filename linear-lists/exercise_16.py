class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_circular(head):
    if head is None:
        return 0
    count = 1
    cur = head.next
    while cur is not None and cur is not head:
        count += 1
        cur = cur.next
    return count

def build_circular(vals):
    if not vals:
        return None
    head = Node(vals[0])
    tail = head
    for v in vals[1:]:
        n = Node(v)
        tail.next = n
        tail = n
    tail.next = head
    return head

def main():
    c = build_circular([10,20,30])
    print("circular count:", count_circular(c))  # 3
    print("empty circular:", count_circular(None))

if __name__ == "__main__":
    main()
