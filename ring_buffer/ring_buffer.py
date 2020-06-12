class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # To make a fixed size array: we have to pad it out with 'None' as each item within its capacity (5)
        self.storage = [None] * capacity
        # The index of items as we go through the list
        self.curr_index = 0

    def append(self, item):

        # print(self.storage)
        # first item 'a' it will get assigned the  index (0) --> as thats the default index set in our bufferclass
        self.storage[self.curr_index] = item
        # print(self.storage[0], 'first item')

        if (self.curr_index + 1) == self.capacity:
            # We make the current item's (newest item) index to the oldest item
            self.curr_index = 0

        else:
            # If capacity not reached, condition is hit until capacity is reached
            # moves index along
            self.curr_index += 1

        return item

    def get(self):
        all_items = []

        for item in self.storage:
            if item is not None:
                all_items.append(item)

        return all_items


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
