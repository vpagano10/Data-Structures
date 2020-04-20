from doubly_linked_list import DoublyLinkedList


# FIFO
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # The list will be changing constantly, and in addition is is faster to add/remove items from the beginning of a linked list than an array because the elements do not need to "shift". We also do not need to lookup specific items, so the benefit of the indexing of an array does not help here.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # length += 1
        self.size = + 1
        # add an item to the end of the list, add_to_tail
        self.storage.add_to_tail(value)

    def dequeue(self):
        # if no head node, return none
        if not self.storage.head:
            return None
        else:
            # decrease by 1, by removing head
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
