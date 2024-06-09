from Node import Node


class HuffmanTree:

    def __init__(self, distribution_map):
        self.distribution_map = dict(distribution_map)
        self.root = None
        self.subtrees = []
        self.result = dict()
        self.result_reversed = dict()

        # convert letters to nodes-subtrees
        self.convert_to_subtrees()
        # merge subtrees
        self.merge_subtrees()
        # assign codes to tree leafs
        self.assign_codes_and_produce_dictionary()
        # reverse result dictionary for decoding purposes
        self.reverse_dictionary()

    def convert_to_subtrees(self):
        for (key, value) in zip(self.distribution_map.keys(), self.distribution_map.values()):
            node = Node(value, key)
            self.subtrees.append(node)

    def merge_subtrees(self):
        # rule 1 : subtree with smaller weight is always left child
        # rule 2 : if the weights are equal letter with lexicographically higher order is left child
        while len(self.subtrees) != 1:
            # left
            left_subtree = self.find_the_smallest_one()
            self.subtrees.remove(left_subtree)
            # right
            right_subtree = self.find_the_smallest_one()
            self.subtrees.remove(right_subtree)
            # create parent
            parent = Node(weight=(left_subtree.weight + right_subtree.weight), letter=left_subtree)
            parent.left = left_subtree
            parent.right = right_subtree
            # add new subtree to subtree list
            self.subtrees.append(parent)

        self.root = self.subtrees.pop()

    def find_the_smallest_one(self):
        equally_small = []
        # find the smallest one by weight
        min_weight = min([node.weight for node in self.subtrees])
        for node in self.subtrees:
            if node.weight == min_weight:
                equally_small.append(node)
        # find the one with lexicographically the highest order among the ones with min weight
        lexicographically_min = min([node.letter for node in equally_small])
        for node in equally_small:
            if node.letter == lexicographically_min:
                return node

    def assign_codes_and_produce_dictionary(self):
        # walk tree depth search in-order and store codes and letters in map
        self.walk_and_label(self.root, self.result)

    def walk_and_label(self, current_node, result):
        if current_node.is_leaf():
            result[current_node.letter] = current_node.code
            return
        # label left child
        current_node.left.code = current_node.code + "0"
        self.walk_and_label(current_node.left, result)
        # label right child
        current_node.right.code = current_node.code + "1"
        self.walk_and_label(current_node.right, result)

    def encode_sequence(self, sequence):
        encoded_sequence = str()
        for letter in str(sequence):
            encoded_sequence += str(self.result[letter])
        return encoded_sequence

    def decode_sequence(self, coded_sequence):
        original_sequence = str()
        coded_letter = ""
        for digit in coded_sequence:
            coded_letter += digit
            if coded_letter in self.result_reversed.keys():
                original_sequence += self.result_reversed[coded_letter]
                coded_letter = ""
        return original_sequence

    def reverse_dictionary(self):
        reversed_dict = dict()
        for key, value in zip(self.result.keys(), self.result.values()):
            reversed_dict[value] = key
        self.result_reversed = reversed_dict
