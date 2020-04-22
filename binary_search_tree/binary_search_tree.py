from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self.value
        if value < node:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value, and False if it does not
    def contains(self, target):
        node = self.value
        if node == target:
            return True
        if target < node:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        node = self.value
        if self.right:
            return self.right.get_max()
        else:
            return node

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        node = self.value
        cb(node)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(node.value)
        if self.right:
            self.right.in_order_print(self.right)
        print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue (imported)
        # add root to queue
        Queue().enqueue(node)
        # while queue not empty
        while Queue().size > 0:
            # node = head of queue
            popped = Queue().dequeue()
            # print node / return node if search value = target
            print(popped.value)
            # add children of node to queue
            if popped.left:
                Queue().enqueue(popped.left)
            if popped.right:
                Queue().enqueue(popped.right)
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create stack (imported)
        # add root to stack
        Stack().push(node)
        # while stack not empty
        while Stack().size > 0:
            # node = pop head of stack
            popped = Stack().pop()
            # print node / return node if search value = target
            print(popped.value)
            # add children of node to stack
            if popped.left:
                Stack().push(popped.left)
            if popped.right:
                Stack().push(popped.right)
        return

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
