class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, node_head):
        self.head = node_head

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.get_next()
        return length

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += str(current) + ' -> '
            current = current.get_next()
        return output

    def pop(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError('Unable to pop from empty list')

    def contains(self, value):
        current = self.head
        while current:
            if current.get_data() == value:
                return True
            else:
                current = current.get_next()
        return False

    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.get_data() == value:
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
            else:
                previous = current
            current = current.get_next()

    def push(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.set_head(new_node)

    def append(self, value):
        current = self.head
        new_node = Node(value)
        if not current:
            self.head = new_node
            return

        while current.get_next():
            current = current.get_next()

        self.head.set_next(new_node)
