from doubly_linked_list import DoublyLinkedList


# FILO
class Stack:
    def __init__(self, node=None):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # When the data set is changing very often, it makes more sense to use a linked list over an array because it is faster for the elements to be removed or deleted from the linked list. We also do not need to look for specific elements, we just need the last one in this case.
        self.storage = DoublyLinkedList()

    def push(self, value):
        # length += 1
        self.size += 1
        # add node to tail
        self.storage.add_to_tail(value)

    def pop(self):
        # if no tail just return
        if not self.storage.tail:
            return None
        # if there is a tail, remove it
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
