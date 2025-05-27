# tests/test_tst.py

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
def test_prefix_words_are_found():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    unique_words = set(words)
    for word in unique_words:
        for i in range(len(word) - 1, 0, -1):
            prefix = word[:i]
            if prefix in unique_words:
                assert tst.search(prefix), f"Prefix word '{prefix}' not found"

def test_non_inserted_prefixes_are_not_found():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    unique_words = set(words)
    for word in unique_words:
        for i in range(len(word), 0, -1):
            prefix = word[:i]
            if prefix not in unique_words:
                assert not tst.search(prefix), f"False positive on: {prefix}"

def test_all_strings_returns_sorted_unique_words():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    unique_words = set(words)
    tst_words = tst.all_strings()
    assert sorted(list(unique_words)) == tst_words, "all_strings() does not return the expected word list"

def test_len_returns_number_of_unique_words():
    base_dir = os.path.dirname(__file__)
    words = load_words(os.path.join(base_dir, '../data/insert_words.txt'))
    tst = TernarySearchTree()
    for word in words:
        tst.insert(word)
    unique_words = set(words)
    assert len(tst) == len(unique_words), f"__len__() returned {len(tst)}, expected {len(unique_words)}"

