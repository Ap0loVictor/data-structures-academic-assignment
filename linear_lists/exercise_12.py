class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedStack:
    def __init__(self):
        self._top = None

    def push(self, x):
        n = Node(x)
        n.next = self._top
        self._top = n

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        v = self._top.data
        self._top = self._top.next
        return v

    def top(self):
        return None if self._top is None else self._top.data

    def is_empty(self):
        return self._top is None


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, x):
        n = Node(x)
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

    def enqueue(self, x):
        if self._size == len(self._data):
            raise OverflowError("queue is full")
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = x
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        v = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return v

    def first(self):
        return None if self._size == 0 else self._data[self._front]

    def is_empty(self):
        return self._size == 0


class LinkedDeque:
    def __init__(self):
        self._head = None
        self._tail = None

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
