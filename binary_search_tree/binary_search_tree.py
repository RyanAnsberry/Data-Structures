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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(5)

# bst.insert(2)

# bst.insert(3)

# bst.insert(7)
# bst.insert(20)
# bst.insert(6)

# print(f"True: {bst.contains(5)}")
# print(f"True: {bst.contains(3)}")
# print(f"False: {bst.contains(1)}")
# print(f"True: {bst.contains(2)}")
# print(f"True: {bst.contains(7)}")
# print(f"Fasle: {bst.contains(8)}")
# print(f"True: {bst.contains(6)}")

# print(f"{bst.get_max()}")


