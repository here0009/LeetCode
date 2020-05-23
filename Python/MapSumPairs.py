"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.records = dict()

    def insert(self, key: str, val: int) -> None:
        self.records[key] = val
        

    def sum(self, prefix: str) -> int:
        res = 0
        for k,v in self.records.items():
            if k.startswith(prefix):
                res += v
        return res

class TrieNode():
    def __init__(self):
        self.count = 0
        self.children = {}

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        curr = self.root
        curr.count += delta
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c] 
            curr.count += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
obj.insert("app", 2)
print(obj.sum("a"))