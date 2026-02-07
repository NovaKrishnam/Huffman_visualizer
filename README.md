# Huffman Visualizer 

A Python-based tool that implements the **Huffman Coding algorithm** to perform lossless data compression. This project provides a visual bridge between abstract greedy algorithms and tangible data reduction.

###  Project Domain: Data Compression & Information Theory

---

##  Features
* **Optimal Prefix Encoding:** Automatically generates the most efficient binary codes based on character frequency.
* **Dynamic Visualization:** Renders the Huffman Tree structure using `NetworkX` and `Matplotlib`.
* **Performance Metrics:** Calculates the **Compression Ratio** to demonstrate the effectiveness of the algorithm.

##  Built With
* **Python 3.x**
* **NetworkX & Matplotlib:** For graph generation and visualization.
* **Pydot:** For Graphviz layout rendering.
* **Heapq:** Min-priority queue implementation for greedy node merging.

---

##  Usage
1. Install dependencies: `pip install networkx matplotlib pydot`
2. Run the script: `python huffman_visualizer.py`
3. Enter your text and view the generated codes and tree.
