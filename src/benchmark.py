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
def run_benchmark():
    """Run the complete benchmark"""
    # Load data
    data_path = "data/corncob_lowercase.txt"
    words = load_corpus(data_path)
    
    if not words:
        print("No words loaded. Exiting.")
        return
    
    print("Running benchmark...")
    print("n\tinsert_s\tsearch_s")
    
    results = []
    test_sizes = [1000, 5000, 10000, 20000, 50000]
    
    for n in test_sizes:
        if n > len(words):
            print(f"Skipping n={n} (not enough words)")
            continue
            
        insert_time = time_insert(words, n)
        search_time = time_search(words, n)
        
        print(f"{n}\t{insert_time:.4f}\t{search_time:.4f}")
        results.append((n, insert_time, search_time))
    
    return results

def plot_results(results):
    """Create and display benchmark plot"""
    if not results:
        print("No results to plot")
        return
    
    ns, insert_times, search_times = zip(*results)
    
    plt.figure(figsize=(10, 6))
    plt.plot(ns, insert_times, 'b-o', label="Insert", linewidth=2)
    plt.plot(ns, search_times, 'r-s', label="Search", linewidth=2)
    plt.xlabel("Number of words (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Ternary Search Tree Performance")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)
    
    # Save plot
    plt.savefig("results/benchmark_plot.png", dpi=300, bbox_inches='tight')
    print("Plot saved to results/benchmark_plot.png")
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    results = run_benchmark()
    if results:
        plot_results(results)
