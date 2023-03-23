class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            current = current.children[c]
        current.is_word = True

    def search(self, word):
        current = self.root
        for c in word:
            if not current.children.get(c):
                return False
            current = current.children[c]
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if not current.children.get(c):
                return False
            current = current.children[c]
        return True
