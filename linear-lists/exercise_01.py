class ArrayStack:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return f"ArrayStack({self._data})"

    def __len__(self):
        return len(self._data)
    
    def push(self, value):
        self._data.append(value)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        return None if not self._data else self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

class ArrayQueue:
    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._head = 0
        self._size = 0

    def __repr__(self):
        items = [self._data[(self._head + i) % self._capacity()] for i in range(self._size)]
        return f"ArrayQueue({items})"

    def _capacity(self):
        return len(self._data)

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity()]
        self._data = new_data
        self._head = 0

    def enqueue(self, value):
        if self._size == self._capacity():
            self._resize(2 * self._capacity())
        tail = (self._head + self._size) % self._capacity()
        self._data[tail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity()
        self._size -= 1
        if 0 < self._size <= self._capacity() // 4:
            self._resize(max(8, self._capacity() // 2))
        return value

    def first(self):
        return None if self._size == 0 else self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

class ArrayDeque:
    """Double-ended queue (deque) implemented with circular buffer."""
    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._head = 0
        self._size = 0

    def __repr__(self):
        items = [self._data[(self._head + i) % self._capacity()] for i in range(self._size)]
        return f"ArrayDeque({items})"

    def _capacity(self):
        return len(self._data)

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity()]
        self._data = new_data
        self._head = 0

    def add_first(self, value):
        if self._size == self._capacity():
            self._resize(2 * self._capacity())
        self._head = (self._head - 1) % self._capacity()
        self._data[self._head] = value
        self._size += 1

    def add_last(self, value):
        if self._size == self._capacity():
            self._resize(2 * self._capacity())
        tail = (self._head + self._size) % self._capacity()
        self._data[tail] = value
        self._size += 1

    def remove_first(self):
        if self._size == 0:
            raise IndexError("remove_first from empty deque")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity()
        self._size -= 1
        return value

    def remove_last(self):
        if self._size == 0:
            raise IndexError("remove_last from empty deque")
        tail_index = (self._head + self._size - 1) % self._capacity()
        value = self._data[tail_index]
        self._data[tail_index] = None
        self._size -= 1
        return value

    def first(self):
        return None if self._size == 0 else self._data[self._head]

    def last(self):
        if self._size == 0:
            return None
        tail_index = (self._head + self._size - 1) % self._capacity()
        return self._data[tail_index]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size