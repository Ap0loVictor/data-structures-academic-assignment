class ArrayBinaryTree:
    def __init__(self, capacity=16):
        self._arr = [None] * (capacity + 1)
        self.capacity = capacity

    def _ensure_index(self, index):
        if index <= self.capacity:
            return
        newcap = max(index, 2 * self.capacity)
        newarr = [None] * (newcap + 1)
        for i in range(len(self._arr)):
            newarr[i] = self._arr[i]
        self._arr = newarr
        self.capacity = newcap

    def set(self, index, value):
        if index < 1:
            raise IndexError("index must be >= 1")
        self._ensure_index(index)
        self._arr[index] = value

    def get(self, index):
        if index < 1 or index > self.capacity:
            return None
        return self._arr[index]
    
    @staticmethod
    def from_level_list(level_list):
        T = ArrayBinaryTree(max(16, len(level_list)*2))
        for i, v in enumerate(level_list):
            if v is not None:
                T.set(i+1, v)
        return T