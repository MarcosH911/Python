class HashTable:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hash_value = self.hash_function(key, len(self.slots))

        if not self.slots[hash_value]:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            next_slot = self.rehash(hash_value, len(self.slots))

            while not self.slots[next_slot] and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if not self.slots[next_slot]:
                self.slots[next_slot] = key
                self.data[next_slot] = data

            else:
                self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):

        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
