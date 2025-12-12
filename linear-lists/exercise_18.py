from exercise_12 import Node

def split_positive_negative(head):
    pos_head = pos_tail = None
    neg_head = neg_tail = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = None
        if cur.data >= 0:
            if pos_head is None:
                pos_head = pos_tail = cur
            else:
                pos_tail.next = cur; pos_tail = cur
        else:
            if neg_head is None:
                neg_head = neg_tail = cur
            else:
                neg_tail.next = cur; neg_tail = cur
        cur = nxt
    return pos_head, neg_head

def build(vals):
    head=None; tail=None
    for v in vals:
        n=Node(v)
        if head is None: head=tail=n
        else: tail.next=n; tail=n
    return head

def to_list(h):
    a=[]; cur=h
    while cur:
        a.append(cur.data); cur=cur.next
    return a

def main():
    h = build([3, -1, 4, -2, 0])
    pos, neg = split_positive_negative(h)
    print("positives:", to_list(pos))
    print("negatives:", to_list(neg))

if __name__ == "__main__":
    main()
