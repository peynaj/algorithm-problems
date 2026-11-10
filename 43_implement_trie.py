"""
A trie (pronounced as "try") or prefix tree is a tree data structure
 used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time: O(n)
        Space: O(n)
        Auxiliary Space: O(1)
        """
        curr = self.root
        word = word.lower()
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True
        return

    def search(self, word: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """
        curr = self.root
        word = word.lower()
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end

    def starts_with(self, prefix: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """
        curr = self.root
        prefix = prefix.lower()
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True


def run_tests():
    obj = Trie()

    # Empty string
    assert obj.starts_with("")
    assert obj.search("") is False

    # Duplicate insertion
    obj.insert("apple")
    obj.insert("apple")
    assert obj.search("apple")
    assert obj.search("apple")
    assert not obj.search("app")
    assert obj.starts_with("app")
    obj.insert("app")
    assert obj.search("app")

    # Case sensitivity
    obj.insert("HELLO")
    assert obj.search("hello")

    print("Tests Finished Successfully.")


if __name__ == "__main__":
    run_tests()
