import TextConverter
from HuffmanTree import HuffmanTree

# Set text for encoding
text = "the technique works by creating a binary tree of nodes"

# Resulting distribution dictionary of text converter class
distribution = TextConverter.convert_to_map(text)
# Run huffman tree algorithm on distribution dictionary
huffman_tree = HuffmanTree(distribution)

# Encoded sequence
encoded = huffman_tree.encode_sequence(text)
# Decode encoded sequence back to original
decoded = huffman_tree.decode_sequence(encoded)

# Print result of huffman tree algorithm : letters and assigned codes for them
print("Map of letters and assigned codes :\n" + str(huffman_tree.result))
print("\nEncoded sequence :\n" + encoded)
print("\nDecoded sequence back to original:\n" + decoded)
