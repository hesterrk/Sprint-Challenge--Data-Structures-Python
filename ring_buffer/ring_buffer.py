class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # To make our fixed size array: we have to pad it out with 'None' as each item within its capacity (5)
        # [None, None, None, None] and then as we append elements at each index within the capacity it replaces the None value with correct value
        self.storage = [None] * capacity
        # The index of items as we go through the list
        self.curr_index = 0

    def append(self, item):
        pass

    def get(self):
        pass
