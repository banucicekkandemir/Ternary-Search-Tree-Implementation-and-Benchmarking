import time
import os
import sys
import matplotlib.pyplot as plt

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from tst import TernarySearchTree

def load_corpus(path):
    """Load words from file, one word per line"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        print(f"Loaded {len(words)} words from {path}")
        return words
    except FileNotFoundError:
        print(f"Error: Could not find file {path}")
        return []

def time_insert(words, n):
    """Time insertion of n words"""
    if n > len(words):
        print(f"Warning: Only {len(words)} words available, using all")
        n = len(words)
    
    tst = TernarySearchTree()
    start = time.perf_counter()
    for word in words[:n]:
        tst.insert(word)
    end = time.perf_counter()
    return end - start

def time_search(words, n):
    """Time searching n words (after inserting them)"""
    if n > len(words):
        n = len(words)
    
    tst = TernarySearchTree()
    # Insert words first
    for word in words[:n]:
        tst.insert(word)
    
    # Time the search operations
    start = time.perf_counter()
    for word in words[:n]:
        tst.search(word)
    end = time.perf_counter()
    return end - start

