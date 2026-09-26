from __future__ import annotations
from typing import List, Self
from pydantic import BaseModel, Field


class TrieNode(BaseModel):
    """
    Trie Node
    """

    children: List[Self | None] = Field(default=[None] * 26, description="List of children")
    is_end_of_word: bool = Field(default=False, description="Is this a end node?")

    @property
    def is_empty(self) -> bool:
        """
        Check if this node has children
        """
        for i in range(26):
            if self.children[i]:
                return False
        return True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def __len__(self) -> int:
        return self.count_words(self.root)

    def count_words(self, node: TrieNode | None) -> int:
        """
        Count the number of words in this Trie
        """
        if not node:
            return 0
        count = 1 if node.is_end_of_word else 0
        for child in node.children:
            count += self.count_words(child)
        return count

    def search(self, word: str):
        """
        Check if word is in this Trie
        """
        current: TrieNode | None = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current:
                if not current.children[index]:
                    return False
                current = current.children[index]
        if current:
            return current.is_end_of_word
        return False

    def insert(self, word: str):
        """
        Insert word into this Trie
        """
        current: TrieNode | None = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current:
                if not current.children[index]:
                    current.children[index] = TrieNode()
                current = current.children[index]
        if current:
            current.is_end_of_word = True

    def search_prefix(self, word: str) -> bool:
        """
        Check if word is in this Trie
        """
        current: TrieNode | None = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current:
                if not current.children[index]:
                    return False
                current = current.children[index]
        return True

    def remove(self, word: str) -> None:
        """
        Remove word from this Trie
        """

        def _remove(node: TrieNode | None, word: str, depth: int = 0) -> TrieNode | None:

            if not node:
                return None

            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                if node.is_empty:
                    del node
                    node = None
                return node

            index = ord(word[depth]) - ord("a")
            node.children[index] = _remove(node.children[index], word, depth + 1)

            if node.is_empty and not node.is_end_of_word:
                del node
                node = None
            return node

        _remove(self.root, word)
