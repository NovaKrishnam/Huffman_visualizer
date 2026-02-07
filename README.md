# Huffman Visualizer
**Efficient Data Compression and Algorithm Visualization**

A Python-based implementation of the Huffman Coding algorithm designed to bridge the gap between abstract greedy strategies and practical lossless data compression.

---

## Project Overview
This tool automates the process of generating optimal prefix codes based on character frequency. By utilizing a min-priority queue (Min-Heap) and binary tree structures, the project provides a tangible way to analyze how variable-length coding reduces data redundancy.

---

## Key Features
* **Automated Prefix Encoding:** Generates optimal binary codes ensuring no code is a prefix of another.
* **Algorithmic Visualization:** Transforms the generated Huffman Tree into a graphical layout using NetworkX and Matplotlib.
* **Analytical Metrics:** Provides real-time calculation of compression ratios to evaluate efficiency against standard 8-bit encoding.

---

## Technical Stack
* **Language:** Python 3.x
* **Core Libraries:** * `Heapq`: Facilitates the greedy merging process via a Min-Priority Queue.
  * `NetworkX & Matplotlib`: Handles the mapping and rendering of complex tree structures.
  * `Pydot`: Manages Graphviz layouts for hierarchical node positioning.

---

## Usage Instructions
1. **Install Dependencies:**
   ```bash
   pip install networkx matplotlib pydot
