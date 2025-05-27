# tests/test_correctness.py

import os
import sys

# Adjust the path to import the TernarySearchTree class from src/scripts
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from tst import TernarySearchTree

def load_words(filepath):
    with open(filepath, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def test_all_inserted_words_from_file():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    for word in set(words):
        assert tst.search(word), f"{word} should be found"
    assert len(tst) == len(set(words))

def test_not_inserted_words_from_file():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    not_insert_words = load_words(os.path.join(base_dir, '../data/not_insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    for word in not_insert_words:
        assert not tst.search(word), f"{word} should NOT be found"

def test_all_inserted_words_are_found():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    unique_words = set(words)
    for word in unique_words:
        assert tst.search(word), f"{word} not found"

