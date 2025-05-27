# src/tst.py

class TSTNode:
    """
    Node class for Ternary Search Tree (TST).
    Each node holds a character, three children, and a flag for end-of-word.
    """
    def __init__(self, char: str):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end_of_word = False
