# exercise_13.py
from exercise_12 import Node

def penultimate(head):
    if head is None or head.next is None:
        return None
    cur = head
    while cur.next and cur.next.next:
        cur = cur.next
    return cur

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
    a = []; cur = head
    while cur:
        a.append(cur.data); cur = cur.next
    return a

def main():
    h = build([1,2,3,4])
    p = penultimate(h)
    print("list:", to_list(h))
    print("penultimate:", p.data if p else None)

if __name__ == "__main__":
    main()
