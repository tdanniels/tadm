class Trie:
    def __init__(self, words: list[str]):
        self.root = {}
        for word in words:
            current_node = self.root
            for char in word:
                try:
                    current_node = current_node[char]
                except KeyError:
                    next_node = {}
                    current_node[char] = next_node
                    current_node = next_node
            current_node["$"] = True

    def __contains__(self, item: str):
        current_node = self.root
        for char in item:
            try:
                current_node = current_node[char]
            except KeyError:
                return False
        return True

    def is_leaf(self, item: str):
        current_node = self.root
        for char in item:
            try:
                current_node = current_node[char]
            except KeyError:
                return False
        return "$" in current_node
