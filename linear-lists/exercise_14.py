from exercise_12 import Node

def concatenate(L, M):
    if L is None:
        return M
    cur = L
    while cur.next:
        cur = cur.next
    cur.next = M
    return L

def build(vals):
    head = None; tail = None
    for v in vals:
        n = Node(v)
        if head is None:
            head = tail = n
        else:
            tail.next = n; tail = n
    return head

def to_list(head):
    a=[]; cur=head
    while cur:
        a.append(cur.data); cur = cur.next
    return a

def main():
    L = build([1,2,3])
    M = build([4,5])
    R = concatenate(L, M)
    print("concatenated:", to_list(R))
    # print("concat empty L:", to_list(concatenate(None, M))) # If you want to test with empty L

if __name__ == "__main__":
    main()
