from exercise_12 import DNode

class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        n = DNode(x)
        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.next = n; n.prev = self.tail; self.tail = n

    def to_list(self):
        a=[]; cur=self.head
        while cur:
            a.append(cur.data); cur=cur.next
        return a

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None

    def remove_duplicates(self):
        seen = set()
        cur = self.head
        while cur:
            nxt = cur.next
            if cur.data in seen:
                self.remove_node(cur)
            else:
                seen.add(cur.data)
            cur = nxt

def build(vals):
    dll = Doubly()
    for v in vals: dll.append(v)
    return dll

def main():
    dll = build([1,2,3,2,4,1,5])
    print("before:", dll.to_list())
    dll.remove_duplicates()
    print("after: ", dll.to_list())

if __name__ == "__main__":
    main()
