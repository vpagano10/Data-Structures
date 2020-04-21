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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue (imported)
        # add root to queue
        root = self.value
        Queue().enqueue(root)
        # while queue not empty
        while Queue().size:
            # node = head of queue
            node = self.value  # <- should be head of queue
            # print node / return node if search value = target
            print(node)
            # add children of node to queue
            if self.left:
                Queue().enqueue(self.left.value)
            if self.right:
                Queue().enqueue(self.right.value)
            # pop node off of queue
            Queue().dequeue()
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create stack (imported)
        # add root to stack
        root = self.value
        Stack().push(root)
        # while stack not empty
        # Stack().storage() -> points to DLL
        while Stack().size:
            # node = pop head of stack
            node = self.value  # <- should be head of stack
            # print node / return node if search value = target
            print(node)
            Stack().pop()
            # add children of node to stack
            if self.left:
                Stack().push(self.left)
                print(self.left.value)
                Stack().pop()
            if self.right:
                Stack().push(self.right)
                print(self.right.value)
                Stack().pop()
        return

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
