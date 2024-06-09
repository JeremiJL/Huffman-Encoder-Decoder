class Node:
    def __init__(self, weight, letter):
        self.parent = None
        self.left = None
        self.right = None
        self.code = ""
        # represents letter of the leaf OR letter with the highest lexicographical order among subtree
        self.letter = str(letter)
        self.weight = int(weight)

    def is_leaf(self):
        return self.left is None and self.right is None
