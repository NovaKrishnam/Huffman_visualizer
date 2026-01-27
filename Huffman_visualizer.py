import heapq
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import pydot
import matplotlib.image as mpimg

# Node class for Huffman Tree
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman Codes
def generate_codes(root, prefix="", codebook={}):
    if root is None:
        return
    if root.char is not None:
        codebook[root.char] = prefix
    generate_codes(root.left, prefix + "0", codebook)
    generate_codes(root.right, prefix + "1", codebook)
    return codebook

# Encode text
def huffman_encode(text, codebook):
    return ''.join(codebook[char] for char in text)

# Decode text
def huffman_decode(encoded_text, root):
    decoded = ""
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded += current.char
            current = root
    return decoded

# Calculate Compression Ratio
def compression_ratio(original, encoded):
    return (len(encoded) / (len(original) * 8)) * 100

# Visualize Huffman Tree using pydot
def visualize_tree(root):
    G = nx.DiGraph()

    def add_edges(node, parent=None, label=""):
        if node:
            node_id = str(id(node))
            node_label = f"{node.char}:{node.freq}" if node.char else str(node.freq)
            G.add_node(node_id, label=node_label)  # Add readable label here
            if parent is not None:
                G.add_edge(parent, node_id, label=label)
            add_edges(node.left, node_id, "0")
            add_edges(node.right, node_id, "1")

    add_edges(root)

    # Convert to Pydot graph with labels
    dot = nx.nx_pydot.to_pydot(G)
    for edge in dot.get_edges():
        edge.set_fontsize(10)
    for node in dot.get_nodes():
        label = G.nodes[node.get_name()]["label"]
        node.set_label(label)

    dot.write_png("huffman_tree.png")

    # Display the image
    img = mpimg.imread("huffman_tree.png")
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.title("Huffman Tree Visualization")
    plt.tight_layout()
    plt.show()


# Main function
if __name__ == "__main__":
    text = input("Enter text to compress using Huffman Encoding:\n")
    
    root = build_huffman_tree(text)
    codebook = generate_codes(root)
    
    encoded = huffman_encode(text, codebook)
    decoded = huffman_decode(encoded, root)

    print("\nGenerated Huffman Codes:")
    for k, v in codebook.items():
        print(f"{k}: {v}")
    
    print(f"\nEncoded binary string:\n{encoded}")
    print(f"\nDecoded text:\n{decoded}")
    print(f"\nCompression Ratio: {compression_ratio(text, encoded):.2f}%")

    visualize_tree(root) 