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

# WITH DLL

# from DLL import DoublyLinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = DoublyLinkedList()
#         self.curr_node = None

#     def append(self, item):
#         # If there is room in the buffer
#         if self.storage.length < self.capacity:
#             # add item to the end of DLL
#             self.storage.add_to_tail(item)
#             # making newest item the tail node
#             self.curr_node = self.storage.tail
#             # print(self.storage.tail)

#         # If limit is reached
#         if self.storage.length == self.capacity:
#             # print(self.storage)

#             # assigning the node's value to new item
#             self.curr_node.value = item
#             print(self.curr_node)

#             # if the current node we are on is the tail
#             if self.curr_node == self.storage.tail:

#                 # make the new item the head of DLL, overwritting the heads value
#                 self.curr_node = self.storage.head

#             else:
#                 # increment along DLL if its full but the current node is not the tail
#                 self.curr_node = self.curr_node.next
#                 # print(self.curr_node)

    # def get(self):
    #     all_items = []

    #     current = self.storage.head
    #     while current is not None:
    #         all_items.append(current.value)
    #         current = current.next

    #     return all_items


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
