import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# TreeNode
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None # BinarySearchTree
        self.right = None # BinarySearchTree 

    # Insert the given value into the tree
    def insert(self, value):
        # if value is smaller than current node value and left is none, 
        # create a new node to the left
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        # if value is greater or equal to current node value and right is none,
        # create a new node to the right
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        # if value is smaller than current node value, go left
        if value < self.value:
            self.left.insert(value)
        # else value is larger than current node value and goes right
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        curr_node_value = self.value
        # Base Case
        # if equal, return True!
        if target == curr_node_value:
            return True
        # if smaller and left is not None, go left 
        elif target < curr_node_value and self.left is not None:
            return self.left.contains(target)
        # if bigger and right is not None, go right
        elif target > curr_node_value and self.right is not None:
            return self.right.contains(target)
        # If all other conditions fail, return false
        else:
            return False

 

    # Return the maximum value found in the tree
    def get_max(self):
        # if current value.right is none, return current value
        if self.right is None:
            return self.value
        # continue checking right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Use callback function on current value
        cb(self.value)
        # if left value is not none, recurse
        if self.left is not None:
            self.left.for_each(cb)
        # if right value is not none, recurse
        if self.right is not None:
            self.right.for_each(cb)

            
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left 1st
        if node.left is not None:
            node.left.in_order_print(node.left)

        # print value
        print(node.value)

        # go right
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue
        queue = Queue()
        # add current node to queue
        queue.enqueue(node)
        # while queue is not empty
        while queue.size > 0:
            # dequeue node off queue
            node = queue.dequeue()
            # print node
            print(node.value)
            # add its childen
            if node.left is not None:
                # add left (if can)
                queue.enqueue(node.left)
            if node.right is not None:
                # add right (if can)
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node-stack
        stack = Stack()
        # push the current node onto the stack
        stack.push(node)
        # while we have items on the stack
        while stack.size > 0:
            # print the current value and pop it off
            node = stack.pop()
            print(node.value)
            # push the right value of current node if we can
            if node.right is not None:
                stack.push(node.right)

            # push the left value of current node if we can
            if node.left is not None:
                stack.push(node.left)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # check if node exists
        if node:
            # print root first
            print(node.value)
            # then left
            self.pre_order_dft(node.left)
            # then right
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # check if node exists
        if node:
            # left 1st
            self.post_order_dft(node.left)
            # then right
            self.post_order_dft(node.right)
            # finally the root
            print(node.value)


