class DynamicArray:

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):

        if not 0 <= item < self.n:
            return IndexError('Index is out of bounds')
        return self.A[item]

    def append(self, element):
        if self.n >= self.capacity:
            self._resize(self.capacity * 2)

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_capacity

    @staticmethod
    def make_array(new_capacity):
        return (new_capacity * ctypes.py_object)()
