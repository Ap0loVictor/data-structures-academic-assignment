class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self._top = None

    def __repr__(self):
        vals = []
        cur = self._top
        while cur:
            vals.append(cur.data)
            cur = cur.next
        return "LinkedStack(" + repr(vals) + ")"

    def push(self, x):
        n = SNode(x)
        n.next = self._top
        self._top = n

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        v = self._top.data
        self._top = self._top.next
        return v

    def top(self):
        if self._top is None:
            return None
        return self._top.data

    def is_empty(self):
        return self._top is None

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def __repr__(self):
        vals = []
        cur = self._head
        while cur:
            vals.append(cur.data)
            cur = cur.next
        return "LinkedQueue(" + repr(vals) + ")"

    def enqueue(self, x):
        n = SNode(x)
        if self._tail is None:
            self._head = self._tail = n
        else:
            self._tail.next = n
            self._tail = n

    def dequeue(self):
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        v = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return v

    def front(self):
        return None if self._head is None else self._head.data

    def is_empty(self):
        return self._head is None

class CircularQueue:
    def __init__(self, capacity=8):
        if capacity < 1:
            capacity = 1
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def __repr__(self):
        vals = [self._data[(self._front + i) % self.capacity()] for i in range(self._size)]
        return "CircularQueue(" + repr(vals) + ")"

    def capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.capacity()

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue is full")
        avail = (self._front + self._size) % self.capacity()
        self._data[avail] = x
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        v = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return v

    def first(self):
        return None if self.is_empty() else self._data[self._front]

    

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedDeque:
    def __init__(self):
        self._head = None
        self._tail = None

    def __repr__(self):
        vals = []
        cur = self._head
        while cur:
            vals.append(cur.data)
            cur = cur.next
        return "LinkedDeque(" + repr(vals) + ")"
    
    def add_first(self, x):
        n = DNode(x)
        n.next = self._head
        if self._head:
            self._head.prev = n
        else:
            self._tail = n
        self._head = n

    def add_last(self, x):
        n = DNode(x)
        n.prev = self._tail
        if self._tail:
            self._tail.next = n
        else:
            self._head = n
        self._tail = n

    def remove_first(self):
        if self._head is None:
            raise IndexError("remove_first from empty deque")
        v = self._head.data
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        return v

    def remove_last(self):
        if self._tail is None:
            raise IndexError("remove_last from empty deque")
        v = self._tail.data
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        return v

    def first(self):
        return None if self._head is None else self._head.data

    def last(self):
        return None if self._tail is None else self._tail.data

    def is_empty(self):
        return self._head is None

