class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def concatenate(L, M):
    if L is None:
        return M
    cur = L
    while cur.next:
        cur = cur.next
    cur.next = M
    return L

# test
def build(vals):
    h = None
    t = None
    for v in vals:
        n = Node(v)
        if h is None:
            h = t = n
        else:
            t.next = n
            t = n
    return h

def list_to_py(head):
    a = []
    cur = head
    while cur:
        a.append(cur.data)
        cur = cur.next
    return a

def main():
    L = build([1,2,3])
    M = build([4,5])
    R = concatenate(L, M)
    print("concatenated:", list_to_py(R))  
    L2 = None
    R2 = concatenate(L2, M)
    print("concat empty L:", list_to_py(R2))

if __name__ == "__main__":
    main()
