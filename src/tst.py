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


        
class TernarySearchTree:
    """
    Ternary Search Tree data structure for fast word insert and search.
    """
    def __init__(self):
        self.root = None

    def _insert(self, node, word: str, idx: int):
        """
        Helper function for recursive insertion.
        """
        char = word[idx]
        if node is None:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, idx)
        elif char > node.char:
            node.right = self._insert(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                node.is_end_of_word = True
            else:
                node.middle = self._insert(node.middle, word, idx + 1)
        return node

    def insert(self, word: str):
        """
        Insert a word into the tree.
        """
        if not word:
            return
        self.root = self._insert(self.root, word, 0)
    def _search(self, node, word: str, idx: int) -> bool:
        """
        Helper function for recursive search.
        """
        if node is None:
            return False
        char = word[idx]
        if char < node.char:
            return self._search(node.left, word, idx)
        elif char > node.char:
            return self._search(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                return node.is_end_of_word
            return self._search(node.middle, word, idx + 1)

    def search(self, word: str) -> bool:
        """
        Return True if word exists in the tree.
        """
        if not word:
            return False
        return self._search(self.root, word, 0)
