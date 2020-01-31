class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        elif self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.right == None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if not self.left or self.left.value is None:
                return False
            elif self.left.value == target:
                return True
            else:
                return self.left.contains(target)
        elif self.value < target:
            if not self.right or self.right.value is None:
                return False
            elif self.right.value == target:
                return True
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)