"""
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
 

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
"""

from typing import List
class TreeNode:
    def __repr__(self):
        return '{}:{}'.format(self.val, self.children.keys()) 

    def __init__(self, val):
        self.val = val
        self.children = dict()


class Tree:
    def __init__(self):
        self.root = TreeNode(0)

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode(w)
            node = node.children[w]
        node.children['#'] = '#'

    def dfs(self, node):
        if '#' in node.children and len(node.children) == 1:
            return [node.val]
        res = []
        for next_node in node.children.values():
            if next_node != '#':
                res.extend(node.val + string for string in self.dfs(next_node))
        return res


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree = Tree()
        for word in words:
            tree.insert(word[::-1])
        # print(tree.root)
        res = []
        for key in tree.root.children:
            res.extend(tree.dfs(tree.root.children[key]))
        # print(res)
        return len(''.join(res)) + len(res)




from typing import List
class TreeNode:
    def __repr__(self):
        return '{}:{}'.format(self.val, self.children.keys()) 

    def __init__(self, val):
        self.val = val
        self.children = dict()


class Tree:
    def __init__(self):
        self.root = TreeNode(0)

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode(w)
            node = node.children[w]
        node.children['#'] = '#'

    def dfs(self, node):
        if '#' in node.children and len(node.children) == 1:
            return [0]
        res = []
        for next_node in node.children.values():
            if next_node != '#':
                res.extend(1 + k for k in self.dfs(next_node))
        return res


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree = Tree()
        for word in words:
            tree.insert(word[::-1])
        res = tree.dfs(tree.root)
        # print(res)
        return sum(res) + len(res)

S = Solution()
words = ["time", "me", "bell", "kme"]
print(S.minimumLengthEncoding(words))
words = ["time", "me", "bell"]
print(S.minimumLengthEncoding(words))