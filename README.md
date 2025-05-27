# Ternary Search Tree

A Python implementation of a Ternary Search Tree (TST) for efficient word storage and search.

## What is it?

A data structure that stores words efficiently and searches them quickly - like a smart dictionary.


## Installation

```bash
git clone https://github.com/banucicekkandemir/Ternary-Search-Tree-Implementation-and-Benchmarking/tree/main
cd Ternary-Search-Tree-Implementation-and-Benchmarking
```
## Usage

```python
from src.tst import TernarySearchTree

# Create tree and add words
tree = TernarySearchTree()
tree.insert("cat")
tree.insert("dog")
tree.insert("bird")

# Search for words
print(tree.search("cat"))     # True
print(tree.search("fish"))    # False

# Get all words (sorted)
print(tree.all_strings())     # ['bird', 'cat', 'dog']

# Count words
print(len(tree))              # 3

# String representation
print(str(tree))              # "bird, cat, dog"

# Load words from file
with open('data/insert_words.txt', 'r') as f:
    for line in f:
        word = line.strip()
        if word:
            tree.insert(word)
```
## Performance

### Time Complexity
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| *Insert* | O(L) | L = length of word |
| *Search* | O(L) | L = length of word |
| *Get All Words* | O(N × L) | N = number of words, L = average word length |

### Space Complexity
- *Overall*: O(N × L) where N = number of unique words, L = average word length
- *Efficient*: Words sharing prefixes share nodes, reducing actual memory usage
- *Per Node*: Each node stores one character + 3 pointers + 1 boolean flag


## Files

- `src/tst.py` - Main code
- `tests/test_tst.py` - Tests
- `data/` - Sample word files

## Testing

```bash
# Run tests
pytest

```