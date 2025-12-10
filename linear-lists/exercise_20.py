class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedBase:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        n = DNode(x)
        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def to_list(self):
        a = []
        cur = self.head
        while cur:
            a.append(cur.data); cur = cur.next
        return a

    def reverse(self):
        cur = self.head
        while cur:
            cur.prev, cur.next = cur.next, cur.prev
            cur = cur.prev  
        self.head, self.tail = self.tail, self.head

def main():
    dll = DoublyLinkedBase()
    for v in [1,2,3,4]:
        dll.append(v)
    print("before:", dll.to_list())
    dll.reverse()
    print("after: ", dll.to_list())  
    dll.reverse()
    print("restored:", dll.to_list())

if __name__ == "__main__":
    main()
